# Trading Analysis Bot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**Trading Analysis Bot** is a Telegram chatbot for data-driven analytics of cryptocurrencies market, particularly the Binance exchange. It provides standard technical indicators, social sentiment and developer activities. Market indexes, rankings and statistic metrics based on on-chain transactions across different blockchain networks are also reported.

![avatar.png](img/avatar.png)

## Run on local machine

```
pip install -r requirements.txt
```

```
# For Windows
set TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
set SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
set API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set DB_NAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set DB_USERNAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set DB_HOST=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set DB_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set ADMIN_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set ADMIN_USERNAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
python bot.py
```

```
# For Linux
export TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
export SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
export API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export DB_NAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export DB_USERNAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export DB_HOST=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export DB_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export ADMIN_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export ADMIN_USERNAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
python bot.py
```

## Deployment on Heroku platform

```
heroku create trading-analysis-bot --buildpack heroku/python
heroku buildpacks:add --index 2 https://github.com/numrut/heroku-buildpack-python-talib
heroku config:set TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set DB_NAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set DB_USERNAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set DB_HOST=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set DB_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set ADMIN_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set ADMIN_USERNAME=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
git push heroku master
heroku ps:scale bot=1 
```

## Features

### Fundamental information

```
/i evx
```

```
#EVX
Type: TOKEN
Consensus Protocol: POW
Cryptographic Algorithm: Ethash
Website: https://www.everex.io/
Social Media: 
https://t.me/everexio
https://www.facebook.com/everex.io
https://twitter.com/everexio
Explorers: 
https://etherscan.io/token/0xf3db5fa2c66b7af3eb0c0b782510816cbe4813b8
Market Cap: $10,694,046
Current Price: $0.473188
Issue Price: $0.880000
Issue Date: 2017-10-11
Max Supply: -
Total Supply: 25,000,000
Circulating Supply: 22,600,000
```

### Short-term transactions

```
/s tnt
```

```
#TNTBTC 92,966,054.00 (94.84%)
P: 0.00000730 V: 608.23 VWAP: 0.00000654
30 mins: Buy 12.07 Sell 6.42
15 mins: Buy 8.37 Sell 3.97
5 mins: Buy 4.19 Sell 2.16
#TNTETH 5,059,783.00 (5.16%)
P: 0.00026182 V: 1,194.92 VWAP: 0.00023616
30 mins: Buy 13.32 Sell 12.58
15 mins: Buy 8.04 Sell 2.38
5 mins: Buy 1.76 Sell 1.99
```

### Technical analysis

```
/x btc
```

![x.png](img/x.png)

### Market movement statistics

```
/m
```

```
#MARKET
USDⓈ: 20 (+) 113 (-)
ALTS: 43 (+) 89 (-)
BNB: 63 (+) 30 (-)
BTC: 120 (+) 31 (-)
Tue Jul  2 13:48:21 2019
```

### Altcoin market money flows

```
/e
```
![market.png](img/market.png)

### On-chain exchange flows

```
/b
```

```
*Daily BTC exchange flows*
#Binance: $75M in | $68M out
#Bitmex: $18M in | $7M out
#Bitfinex: $6M in | $8M out
#Bitstamp: $18M in | $22M out
#Bittrex: $2M in | $4M out
#Poloniex: $1M in | $2M out

*Daily ETH exchange flows*
#Binance: $24M in | $12M out
#Bitfinex: $2M in | $1M out
#Bittrex: $240k in | $415k out
#Kraken: $2M in | $2M out
#Kucoin: $406k in | $235k out
#Poloniex: $325k in | $352k out

*Weekly BTC exchange flows*
Inflow: $703.8M (-42.1% from last week)
Outflow: $763.5M (-27.8% from last week)
Net flow: -$59.7M
#BTC price: $8084.63 (-1.3% from last week)

*Weekly ETH exchange flows*
Inflow: $119.1M (-37.5% from last week)
Outflow: $111.8M (-48.7% from last week)
Net flow: $7.3M
#ETH price: $175.74 (+0.8% from last week)

*Weekly Stablecoin exchange flows*
Inflow: $264.3M (-51.1% from last week)
Outflow: $364.0M (-45.7% from last week)
Net flow: -$99.7M
```

![b.png](img/b.png)

### Transaction activities

```
/w USDT mint
```

```
*Transaction activities*
2019-10-12: :dollar:  2,500,000 #USDT (2,494,282 USD) minted at Tether Treasury
2019-10-12: :dollar:  5,000,000 #USDT (5,012,230 USD) minted at Tether Treasury
2019-10-11: :dollar: :dollar:  15,000,000 #USDT (15,077,725 USD) minted at Tether Treasury
2019-10-10: :dollar: :dollar: :dollar:  20,000,000 #USDT (20,002,176 USD) minted at Tether Treasury
2019-10-07: :dollar: :dollar:  12,387,600 #USDT (12,392,934 USD) minted at Tether Treasury
2019-10-07: :dollar: :dollar:  20,000,000 #USDT (19,952,765 USD) minted at Tether Treasury
2019-10-04: :dollar: :dollar:  12,600,000 #USDT (12,725,111 USD) minted at Tether Treasury
2019-10-04: :dollar:  5,000,000 USDT (5,035,628 USD) minted at Tether Treasury
2019-09-30: :dollar: :dollar:  20,000,000 #USDT (19,996,690 USD) minted at Tether Treasury
```

```
/w BTC Binance
```

```
*Transaction activities*
2019-10-16: :rotating_light: :rotating_light:  3,359 #BTC (26,705,730 USD) transferred from #Binance to unknown wallet
2019-10-16: :rotating_light: :rotating_light:  3,000 #BTC (23,834,707 USD) transferred from unknown wallet to #Binance
2019-10-14: :rotating_light: :rotating_light:  3,000 #BTC (24,890,913 USD) transferred from #Binance to #Gemini
2019-10-11: :rotating_light: :rotating_light:  2,721 #BTC (22,854,703 USD) transferred from #Binance to unknown wallet
2019-10-11: :rotating_light: :rotating_light:  2,721 #BTC (22,648,785 USD) transferred from unknown wallet to #Binance
2019-10-11: :rotating_light:  1,300 #BTC (10,937,468 USD) transferred from unknown wallet to #Binance
2019-10-10: 643 #BTC (5,526,899 USD) transferred from #Binance to unknown wallet
2019-10-08: 602 #BTC (4,919,049 USD) transferred from #Binance to unknown wallet
2019-10-08: 1,111 #BTC (9,122,044 USD) transferred from #Binance to unknown wallet
2019-10-07: 659 #BTC (5,413,301 USD) transferred from #Coinbase to #Binance
2019-10-07: 706 #BTC (5,772,057 USD) transferred from #Binance to unknown wallet
```

### Liquidation activities

```
/r XBTUSD
```

```
*Liquidation activities*
2019-11-16 14:14:04: Liquidated long on XBTUSD: Sell 177,058 @ 8462
2019-11-16 14:13:34: Liquidated long on XBTUSD: Sell 40,576 @ 8469
2019-11-16 14:01:44: Liquidated short on XBTUSD: Buy 403,625 @ 8514
2019-11-16 14:01:32: Liquidated short on XBTUSD: Buy 3,536 @ 8507
2019-11-16 14:01:27: Liquidated short on XBTUSD: Buy 1 @ 8500.5
2019-11-16 11:05:44: Liquidated long on XBTUSD: Sell 3,322 @ 8453.5
2019-11-16 10:50:14: Liquidated long on XBTUSD: Sell 72 @ 8460.5
2019-11-16 10:48:24: Liquidated long on XBTUSD: Sell 398,077 @ 8468.5
2019-11-16 10:46:54: Liquidated long on XBTUSD: Sell 13,586 @ 8481.5
2019-11-16 09:29:14: Liquidated short on XBTUSD: Buy 396,629 @ 8527
2019-11-16 09:28:55: Liquidated short on XBTUSD: Buy 289,471 @ 8519
2019-11-16 09:28:50: Liquidated short on XBTUSD: Buy 755,983 @ 8511
2019-11-16 09:28:44: Liquidated short on XBTUSD: Buy 10 @ 8500.5
2019-11-16 07:05:04: Liquidated short on XBTUSD: Buy 134,522 + 248,222 @ 8488.5, 8496
2019-11-16 07:04:44: Liquidated short on XBTUSD: Buy 230 @ 8478
2019-11-16 02:22:34: Liquidated long on XBTUSD: Sell 132,408 @ 8430.5
```

![r.png](img/r.png)

### Newsflow

```
/n
```

```
*Newsflow*
- [Messari Insight] Market signals indifference towards assets listed as likely securities by the Crypto Ratings Council 
- Telegram will delay launch of TON blockchain in light of SEC pressure
- Telegram may be under FinCEN investigation, Libra Association finalizes initial partners
- Nasdaq lists an AI-powered index of crypto market’s top 100 performers
- eToro launches crypto portfolio weighted by twitter mentions
- CoinShares jointly rolls out a gold token ‘DGLD’, built on the bitcoin network #BTC
- Layer1 is seeking $50 million to run wind-powered Bitcoin mining facilities in the US #BTC
- Bitcoin ETF denial, crypto airdrop taxation, the future of Libra, and more
- Grayscale wins approval for first public digital currency index fund #ETH #XRP #LTC #BTC
- [Analysis] Cross-shard DeFi composability - Vitalik Buterin #ETH
- Booking Holdings becomes the latest Libra dropout
- DeFi Week of Oct. 7 - The Defiant
- Telegram said it has been in talks with the SEC about TON "for the past 18 months" #GRAM
- SEC, FinCEN and CFTC issue a 3-party joint statement on digital assets
- Coinbase eyes further European expansion after winning an Irish e-money license
- Zcash to develop a wrapped token for Ethereum #ZEC #ETH
- The Evolution of Crypto Capital Markets
- Incentivizing testnet participation #ATOM #DOT #ETH #TON #ERD #SOL
- Stablecoins backed by national currencies #USDT
- How crypto could fit in your portfolio #BTC #ETH
- Crypto Rates Markets
- Libra, the iTunes App Store for crypto devs
- Crypto Monetary Policies #KMD #VEN #XZC #WAVES #GXS #XMR #REP #ATOM #WTC #ARDR #MANA #TRX #AION #ONT #XRP #XTZ #EOS #BCD #LOOM #BCN #ZEC #STEEM #DCR #MKR #BAT #BTG #DOGE #BNB #VEIL #NANO #NEO
Source: https://messari.io
```

## Licence
MIT

## Support

- Star and/or fork this repository
- Trade on Binance: https://www.binance.com/?ref=13339920
- Trade on FTX: https://ftx.com/#a=1909564
