# Trading bot BTC
## Context
I created a bot that analyze the feelings of the market maker with the help of the fear and greed index (https://alternative.me/crypto/fear-and-greed-index/) that analyze the Volatility, the Market Momentum/Volume, the Social Media (twitter), the Dominance and the Trends (google trends). \
I share with you the utils functions that recover the datas.

I used the module Backtrader to test my strategies. Four inputs were relevant for me : the prices, the volume, the call and puts, and analysis of orders from BTC whale addresses. I used coinglass.com to get these datas.

Obviously I do not show my strategies in this public repository, I just put the utils and framework to create the strategies easily.

## Use it
To use it, you need to install Backtrader :
```bash
pip install backtrader
```
And you need to create an account on https://www.coinglass.com/ and get your coinglass secret key to use the api. You add then your key in the src/config.py file.
