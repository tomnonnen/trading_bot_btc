from cv2 import merge
from config import *
import pandas as pd

long_short_df = pd.read_csv(LONG_SHORT_DATA_FILE)
bitcoin_df = pd.read_csv(BITCOIN_DATA_FILE, sep=';')

long_short_df[LONG_SHORT_DATETIME] = pd.to_datetime(long_short_df[LONG_SHORT_DATETIME])
bitcoin_df[BITCOIN_DATETIME] = pd.to_datetime(bitcoin_df[BITCOIN_DATETIME])

merged_data = long_short_df.merge(bitcoin_df, left_on=LONG_SHORT_DATETIME, right_on=BITCOIN_DATETIME)
merged_data["Long Short Ratio"] = merged_data["Total Long"]/merged_data["Total Short"]
merged_data = merged_data.drop([
    "Noncommercial Long",
    "Noncommercial Short",
    "Noncommercial Spreads",
    "Commercial Long",
    "Commercial Short",
    "Total Long",
    "Total Short",
    "Nonreportable Positions Long",
    "Nonreportable Positions Short",
    "Adj Close",
], axis=1)

merged_data.to_csv(MERGED_DATA_FILE, index=False)