import yfinance as yf
from fredapi import Fred
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class DataLoader:
    def __init__(self):
        self.fred = Fred(api_key=os.getenv("FRED_API_KEY"))

    def fetch_data(self, sector_ticker, start_date="2020-01-01"):
        # 1. Fetch 10Y Treasury Yield (Daily)
        yield_data = self.fred.get_series('DGS10', observation_start=start_date)
        yield_df = pd.DataFrame(yield_data, columns=['yield_rate'])
        
        # 2. Fetch Sector ETF Price
        sector_df = yf.download(sector_ticker, start=start_date)['Adj Close']
        
        # 3. Calculate Daily Returns (The percentage change is what we regress)
        # We use diff() for yield because it's already a percentage, 
        # but pct_change() for stock prices.
        yield_diff = yield_df['yield_rate'].diff().dropna()
        sector_ret = sector_df.pct_change().dropna()
        
        # 4. Aligning Data (The CS Challenge)
        combined = pd.merge(sector_ret, yield_diff, left_index=True, right_index=True, how='inner')
        combined.columns = ['sector_return', 'yield_change']
        
        return combined