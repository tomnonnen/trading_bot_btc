import numpy as np


#==========Utils===========

#SMA : Simple Moving Average
def SMA(arr, window_size=20):
    moving_averages = []
    i=0
    while i < len(arr) - window_size + 1:
    
        # Calculate the average of current window
        window_average = round(np.sum(arr[i:i+window_size]) / window_size, 2)
        
        # Store the average of current
        # window in moving average list
        moving_averages.append(window_average)
        
        # Shift window to right by one position
        i += 1
    return moving_averages

#EMA : Exponential Moving Average
def EMA(arr, window_size=20, smoothing=2):
    ema = [sum(arr[:window_size]) / window_size]
    for price in arr[window_size:]:
        ema.append((price * (smoothing / (1 + window_size))) + ema[-1] * (1 - (smoothing / (1 + window_size))))
    return ema  

#MACD : Moving Average Convergence/Divergence
def MACD(arr, val1, val2):
    return EMA(arr, val1) - EMA(arr, val2)

#BB : Bollinger Band
def BB(arr, window_size=20):
    sma = SMA(arr, window_size)
    std = arr.rolling(window_size).std()
    bollinger_up = sma + std * 2
    bollinger_down = sma - std * 2
    return bollinger_up, bollinger_down

#BBW : Bollinger Band Width
def BBW(arr, window_size=20):
    (upper_bound, lower_bound) = BB(arr, window_size)
    middle_bound = SMA(arr, window_size)
    return (upper_bound - lower_bound)/middle_bound

#HH_LL : Highest High & Lowest Low
def HH_LL(arr_HH, arr_LL, window_size=20):
    return (SMA(arr_HH, window_size), SMA(arr_LL, window_size))

#=======Strategies=======

#codes
#1 : buy
#0 : no trades
#-1 : sell

#he finds (val1, val2) = (26, 12)
def SMA_Crossover(arr, idx, val1, val2):
    fast_sma = SMA(arr, val1)
    slow_sma = SMA(arr, val2)
    if(fast_sma[idx] > slow_sma[idx]): return 1
    return 0

#he finds (val1, val2, val3) = (12, 26, 9)
def MACD_Crossover(arr, idx, val1, val2, val3):
    macd = MACD(arr, val1, val2)
    sma = SMA(arr, val3)
    if(sma[idx] > macd[idx]): return 1
    return 0

def BB_Crossover(arr, idx, window_size):
    (upper_bound, lower_bound) = BB(arr, window_size)
    if(arr[idx] > upper_bound[idx]):
        return 1
    elif(arr[idx] < lower_bound[idx]):
        return -1
    return 0

class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma = btind.SimpleMovingAverage(period=15)

    def next(self):
        if self.sma > self.data.close:
            # Do something
            pass

        elif self.sma < self.data.close:
            # Do something else
            pass