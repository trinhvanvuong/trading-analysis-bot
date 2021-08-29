import os
import telegram
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
from binance_trading_bot.client import Client
from binance_trading_bot import analysis, market, owl
import tweepy

INTRO_TEXT = """
*Alpha Crypto* is the most innovative crypto community in Vietnam, providing top-notch market insights and trading signals 
► [Website](https://alphacrypto.tech)
► [Channel: +3,000 followers](https://t.me/AlphaCryptoX)
► [Community: +10,000 members](https://t.me/AlphaCryptoTrading)
► [Twitter: +50,000 followers](https://twitter.com/AlphaCryptoX)

*Services*
► [Private Group: Crypto Derivatives](https://alphacrypto.tech/private-group)
► [Mentor Program: Technical Analysis](https://alphacrypto.tech/mentor-program)
► [Software: Trading Analysis Bot](https://alphacrypto.tech/trading-analysis-bot)

*Promotions*
► [Binance Exchange: +50USDT & -20% trading fee](https://www.binance.com/en/register?ref=39254198)
► [Binance Futures: +100USDT & -15% trading fee](https://www.binance.com/en/futures/ref/alphacrypto)
► [FTX Exchange: +35USD & -10% trading fee](https://ftx.com/#a=AlphaCrypto)
► [Brave Browser: Free BAT](https://brave.com/tpc256)

*Contact* @KakalotZ ([Subscription](https://alphacrypto.tech/subscription))
"""

MANUAL_TEXT = """
Data-driven analytics of crypto-market.

*Fundamental information*
Syntax: /i <asset>
Usage: /i oax or /i algo bnb.
*Short-term transactions*
Syntax: /s <asset>
Usage: /s qtum or /s btt fet.
*Technical analysis*
Syntax: /x <asset> <n-step> <time-step> <time-frame> <time-window>
Usage: /x fet celrusdt or /x dlt 4h 30 or /x evx 25 5m 1h 1. 
*Exchange on-chain flows*
Syntax: /b
*Market movement statistics*
Syntax: /m
*Altcoin market scan*
Syntax: /a <n-pairs>
Usage: /a 15.
*Altcoin market money flows*
Syntax: /e <n-day>
Usage: /e or /e 90.
*Transaction activities*
Syntax: /w <keyword>
Usage: /w USDT mint or /w BTC Binance.
*Liquidation activities*
Syntax: /r <keyword>
Usage: /r long XBTUSD or /r ETHUSD or /r.
*News*
Syntax: /n

Copyright: @KakalotZ 
 """

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_ADMIN_USERNAME = os.environ['TELEGRAM_ADMIN_USERNAME']
TELEGRAM_ADMIN_CHATID = os.environ['TELEGRAM_ADMIN_CHATID']

twitterAuth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
twitterAuth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
twitterApi = tweepy.API(twitterAuth)

client = Client(os.environ['BINANCE_API_KEY'], os.environ['BINANCE_SECRET_KEY'])

# Altcoin scan
def a(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        market.altcoin_scan(client)
        bot.send_document(chat_id=update.message.chat_id, document=open('data/market_list_btc.csv', 'rb'))
        bot.send_document(chat_id=update.message.chat_id, document=open('data/market_list_usdt.csv', 'rb'))

# Fundamental information
def i(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        for asset in args:
            asset = asset.upper()
            msg = analysis.asset_info(client, asset)
            bot.send_message(chat_id=update.message.chat_id, 
                             text=msg, 
                             parse_mode=ParseMode.MARKDOWN, 
                             disable_web_page_preview=True)

# Short-term transactions
def s(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    for asset in args:
        asset = asset.upper()
        msg = analysis.asset_analysis(client, asset)
        bot.send_message(chat_id=update.message.chat_id, 
                         text=msg, 
                         parse_mode=ParseMode.MARKDOWN, 
                         disable_web_page_preview=True)

# Technical analysis
def x(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        NUM_PRICE_STEP = 40
        TIME_FRAME_STEP = '1h'
        TIME_FRAME = '1d'
        TIME_FRAME_DURATION = '60 days ago UTC'
        if args[-1][0].isdigit():
            if args[-1][-3:]=='UTC':
                TIME_FRAME_DURATION = args[-1].replace('_', ' ')
            else:
                TIME_FRAME_DURATION = args[-1]+' days ago UTC'
        try:
            if args[-2][0].isdigit():
                TIME_FRAME = args[-2]
        except Exception:
            pass
        try:
            if args[-3][0].isdigit():
                TIME_FRAME_STEP = args[-3]
        except Exception:
            pass
        try:
            if args[-4][0].isdigit():
                NUM_PRICE_STEP = int(args[-4])
        except Exception:
            pass
        coinList = []
        for arg in args:
            if not arg.isdigit():
                coinList.append(arg)
            else:
                break
        for coin in coinList:
            coin = coin.upper()
            for MARKET in [coin, coin+'BTC', coin+'USDT']:
                owl.volume_spread_analysis(client, MARKET, NUM_PRICE_STEP, TIME_FRAME_STEP, TIME_FRAME, TIME_FRAME_DURATION)
                bot.send_photo(chat_id=update.message.chat_id, 
                           photo=open('img/'+MARKET+'_'+TIME_FRAME.upper()+'.png', 'rb'))

# Exchange on-chain flows
def b(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        msg = analysis.exchange_flows(twitterApi)
        bot.send_message(chat_id=update.message.chat_id, 
                         text=msg, 
                         parse_mode=ParseMode.MARKDOWN, 
                         disable_web_page_preview=True)
        analysis.exchange_flows_visual(twitterApi)
        bot.send_photo(chat_id=update.message.chat_id, 
                   photo=open('img/bitcoin_exchange_flows.png', 'rb'))
                   
# Transaction activities
def w(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        msg = analysis.transaction_activities(twitterApi, args)
        bot.send_message(chat_id=update.message.chat_id, 
                         text=msg, 
                         parse_mode=ParseMode.MARKDOWN, 
                         disable_web_page_preview=True)
                         
# Liquidation activities
def r(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        msg = analysis.liquidation_activities(twitterApi, args)
        if len(args)==0:
            bot.send_photo(chat_id=update.message.chat_id, 
                       photo=open('img/bitmex_liquidations.png', 'rb'))
        else:
            bot.send_message(chat_id=update.message.chat_id, 
                             text=msg, 
                             parse_mode=ParseMode.MARKDOWN, 
                             disable_web_page_preview=True)

# Market movement statistics
def m(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        msg = market.market_change(client)
        bot.send_message(chat_id=update.message.chat_id, 
                         text=msg, 
                         parse_mode=ParseMode.MARKDOWN, 
                         disable_web_page_preview=True)

# Altcoin market money flows
def e(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        try:
            timeInterval = int(args[0])
        except Exception:
            timeInterval = 120
        market.market_movement(client, timeInterval)
        bot.send_photo(chat_id=update.message.chat_id, 
                   photo=open('img/market.png', 'rb'))

# Newsflow
def n(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    msg = analysis.newsflow()
    bot.send_message(chat_id=update.message.chat_id, 
                     text=msg, 
                     parse_mode=ParseMode.MARKDOWN, 
                     disable_web_page_preview=True)
    
# BTC
def v(bot, update, args):
    if str(update.message.from_user.username)==TELEGRAM_ADMIN_USERNAME:
        try:
            market = args[0].upper()+'USDT'
        except Exception:
            market = 'BTCUSDT'
        x(bot, update, [market, '40', '1m', '15m', '2'])
        x(bot, update, [market, '40', '3m', '30m', '4'])
        x(bot, update, [market, '40', '5m', '1h', '7'])
        x(bot, update, [market, '40', '15m', '2h', '15'])
        x(bot, update, [market, '40', '30m', '4h', '30'])
        x(bot, update, [market, '40', '30m', '6h', '45'])
        x(bot, update, [market, '40', '1h', '12h', '60'])
        x(bot, update, [market, '40', '1h', '1d', '120'])

# Manual
def manual(bot,update):
    bot.send_message(chat_id=update.message.chat_id, 
                     text=MANUAL_TEXT, 
                     parse_mode=ParseMode.MARKDOWN, 
                     disable_web_page_preview=True)
    bot.send_message(chat_id=update.message.chat_id, 
                     text=INTRO_TEXT, 
                     parse_mode=ParseMode.MARKDOWN, 
                     disable_web_page_preview=True)
                     
def main():
    updater=Updater(TELEGRAM_TOKEN)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", manual))
    dp.add_handler(CommandHandler("help", manual))
    dp.add_handler(CommandHandler("m", m))
    dp.add_handler(CommandHandler("n", n))
    dp.add_handler(CommandHandler("v", v, pass_args=True))
    dp.add_handler(CommandHandler("i", i, pass_args=True))
    dp.add_handler(CommandHandler("w", w, pass_args=True))
    dp.add_handler(CommandHandler("r", r, pass_args=True))
    dp.add_handler(CommandHandler("b", b))
    dp.add_handler(CommandHandler("a", a))
    dp.add_handler(CommandHandler("e", e, pass_args=True))
    dp.add_handler(CommandHandler("x", x, pass_args=True))
    dp.add_handler(CommandHandler("s", s, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()