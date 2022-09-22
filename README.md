# Trading bot BTC
## Context
This bot analyzes the feelings of the market with the help of the fear and greed index (https://alternative.me/crypto/fear-and-greed-index/). The fear and greed index analyzes the Volatility, the Market Momentum/Volume, the Social Media (twitter), the Dominance and the Trends (google trends). 

The module Backtrader is used to test the strategies. Five inputs were relevant : the fear and greed, the prices, the volume, the call and puts, and the order book from BTC whale addresses. 

This repository provides the utils functions to get and organize the data and allows to put it into Backtrader to implement various different strategies.
https://www.coinglass.com/ is used to get these data.

## Use it
To use it, you need to install Backtrader :
```bash
pip install backtrader
```
And you need to create an account on https://www.coinglass.com/ and get your coinglass secret key to use the api. You add your key in the src/config.py file.
