import datetime
import os
import sys

# configuration constants
from config import *

# import the backtrader platform
import backtrader as bt
from GenericCSV_LongShort import GenericCSV_LongShort

# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].longshortratio

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

if __name__=="__main__":
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, MERGED_DATA_FILE)

     # Create a Data Feed
    data = GenericCSV_LongShort(
        dataname=datapath,
        nullvalue=0.0,
        dtformat=('%Y-%m-%d'),
        datetime=0,
        open=2,
        high=3,
        low=4,
        close=5,
        volume=6,
        openinterest=1,
        longshortratio=7
    )

    cerebro.adddata(data)

    # desired cash start
    cerebro.broker.setcash(100000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())