import json
import pandas as pd
from api_etl.etl import *
from api_etl.benzinga import *
from api_etl.yahoofinance import *
from api_etl.fred import *
from api_etl.youtube import *
from api_etl.alphavantage import *
from api_etl.eia import *

# working directory should be the same as this file
if __name__ == "__main__":
    with open("../api-keys.json", "r") as f:
        api_keys = json.load(f)
        print(f"Found keys for {', '.join(api_keys.keys())}")

    fromdate = "1940-01-01"
    todate = "2023-09-16"
    
    #-------------------------uncomment below to fetch data------------------------------

    #------------------------------pull Benziga news data--------------------------------
    # completed_list = ['MSFT', 'JNJ', 'INTC', 'BA', 'UNH', 
    #         'JPM', 'V', 'PG', 'HD', 'CVX', 
    #         'MRK', 'KO', 'CSCO', 'MCD','WMT', 
    #         'CRM', 'DIS', 'VZ', 'NKE', 'AAPL', 
    #         'IBM', 'GS', 'HON', 'AXP', 'AMGN']

    # # cut the size to lower down gpt budget
    # # for the reference, 11 sections in sp500 include:
    # # Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Health Care, Financials, Information Technology, Communication Services, Utilities, Real Estate
    # tick_list = ['MSFT', 'AAPL', # Tech ('INTC', 'CRM', 'IBM')
    #              'JNJ', 'UNH', # Health care ('MRK','AMGN')
    #              'JPM', # Financials ('GS','AXP','V')
    #              'BA', # Industrials ('HON')
    #              'WMT', # Consumer Staples ('PG'，'KO')
    #              'NKE', # Consumer Discretionary ('HD', 'MCD')
    #              'CVX', # Energy
    #              'VZ', # Communication Services ('DIS')
    #             ]
    
    # Benzinga.pull_batch_benzinga(api_keys, tick_list, fromdate, todate)
    
    #------------------------------pull yahoo stock data---------------------------------
    tick_list = ['^DJI', 'MT', 'NUE', 'X', 'STLD', 
                 'PKX', 'RS', 'GGB', 'CMC', 'CLF',
                 'SCHN', 'ATI', 'SID', 'CRS', 'TMST',
                 'ZEUS']

    yahoo = Yahoo(tick_list, api_keys, fromdate, todate)
    yahoo.fetch_data()
    # yahoo.add_technical_indicators()
    yahoo.add_vix()
    yahoo.add_bond()
    yahoo.export_as_ts_ref()
    ## yahoo.export_as_csv()
    #------------------------------pull yahoo stock data---------------------------------
    # tick = 'NVDA'
    # alpha = Alphavantage(api_keys)
    # alpha.fetch_earning_data(tick)

    #----------------------------pull macro economics data-------------------------------
    # fred = Fredapi(api_keys, fromdate, todate)
    # fred.fetch_macro_data()
    # fred.fetch_steel_data()
    
    #----------------------------pull eia energy & climate data-------------------------------
    # eia = Eia()
    # eia.fetch_energy_climate_data()

    #----------------------------pull youtube data-------------------------------
    # tube = Youtube(api_keys = api_keys, channel_name = 'The Stocks Channel', start_day = fromdate, end_day = todate)
    # tube.get()
    





