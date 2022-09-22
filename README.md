# Trading bot BTC
## Context
This bot analyzes the feelings of the market maker with the help of the fear and greed index (https://alternative.me/crypto/fear-and-greed-index/) that analyze the Volatility, the Market Momentum/Volume, the Social Media (twitter), the Dominance and the Trends (google trends). \
This repository share the utils functions that can recover and organize these datas into Backtrader to let set up strategies.

The module Backtrader is used to test the strategies. Four inputs were relevant : the prices, the volume, the call and puts, and analysis of orders from BTC whale addresses. \
https://www.coinglass.com/ is used to get these datas.

## Use it
To use it, you need to install Backtrader :
```bash
pip install backtrader
```
And you need to create an account on https://www.coinglass.com/ and get your coinglass secret key to use the api. You add then your key in the src/config.py file.
