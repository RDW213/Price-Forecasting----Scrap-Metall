from fredapi import Fred
from api_etl.etl import ETL
import pandas as pd

class Fredapi(ETL):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.macro_indices = ["PAYEMS", "FEDFUNDS", "UNRATE", "PPIACO", "CPIAUCSL",
                        "PCE", "INDPRO", "UMCSENT", "RSAFS", "HOUST", 
                        "CSUSHPINSA", "DAUPSA", "TOTALSA", "PSAVERT", "GPDI", 
                        "BUSINV", "DGORDER", "GS10", "GS5", "GS2", 
                        "RECPROUSM156N", "DTWEXAFEGS", "USSLIND", "T10Y2Y", "GDPC1",
                        "CES0500000017", "TLNRESCONS", "PNRESCONS", "PBNRESCONS"]
        self.steel_indices = ["PIORECRUSDM", "PCU2123122123120", "IPG3311A2NQ", "WPU101707",
                              "WPU10170502", "WPU101", "A31ANO", "IPN3311A2RS"]

    def fetch_macro_data(self):
        fred = Fred(api_key=self.api_keys["Fred"])
        dfs = []

        # Mapping of series IDs to their actual names
        # value contains the list [Index, Description, Unit]
        names = {
        "PAYEMS": ["NFP", "US Non-Farm Payrolls", "Thousands of Persons"], # Non-Farm Payrolls
        "CPIAUCSL": ["CPI", "US Consumer Price Index", "Index 1982-1984=100"], # Consumer Price Index
        "FEDFUNDS": ["InterestRate", "US Effective Federal Funds Rate", "Percent"], # Effective Federal Funds Rate
        "UNRATE": ["UnemploymentRate", "US Unemployment Rate", "Percent"],
        "PPIACO": ["PPI", "US Producer Price Index", "Index 1982=100"], # Producer Price Index
        "PCE": ["PCE", "US Personal Consumption Expenditures", "Billions of Dollars"], # Personal Consumption Expenditures
        "INDPRO": ["IPI", "US Industrial Production Index", "Index 2017=100"], # Industrial Production Index
        "UMCSENT": ["ConsumerSentiment", "US Consumer Sentiment", "Index 1966:Q1=100"],
        "RSAFS": ["RetailSales", "US Retail Sales", "Millions of Dollars"],
        "HOUST": ["HousingStarts", "US New Privately Owned Housing Units Started", "Thousands of Units"], # New Privately Owned Housing Units Started
        "CSUSHPINSA": ["HPI", "US National Home Price Index", "Index Jan 2000=100"], # S&P/Case-Shiller U.S. National Home Price Index
        "DAUPSA": ["DomesticAutoProduction", "US Domestic Auto Vehicle Production", "Thousands of Units"],
        "TOTALSA" : ["TotalVehicleSales", "US Total Vehicle Sales", "Millions of Units"],
        "PSAVERT" : ["PersonalSavingRate", "US Personal Saving Rate", "Percent"],
        "GPDI" : ["GrossPrivateDomesticInvestment", "US Gross Private Domestic Investment", "Billions of Dollars"],
        "BUSINV" : ["TotalBusinessInventories", "US Total Business Inventories", "Millions of Dollars"],
        "DGORDER" : ["ManufacturersNewOrdersDurableGoods", "US Manufacturers New Orders Durable Goods", "Millions of Dollars"],
        "GS10" : ["10YearTreasuryRate", "US 10 Year Treasury Rate", "Percent"],
        "GS5" : ["5YearTreasuryRate", "US 5 Year Treasury Rate", "Percent"],
        "GS2" : ["2YearTreasuryRate", "US 2 Year Treasury Rate", "Percent"],
        "RECPROUSM156N" : ["USRecessionProbabilities", "US Smooth Recession Probabilities", "Percent"],
        "DTWEXAFEGS" : ["USDollarIndex", "Nominal Advanced Foreign Economies U.S. Dollar Index", "Index Jan 2006=100"],
        "USSLIND" : ["IndexLeadingIndicatorsUS", "Index Leading Indicators, US", "Percent"],
        "T10Y2Y" : ["10Y-2YTreasuryCurve", "10-year MINUS 2-year Treasury Curve", "Percent"],
        "GDPC1" : ["USRealGDP", "Real GDP, US", "Billions of Chained 2012 Dollars"],
        "CES0500000017" : ["WeeklyPayrolls","Indexes of Aggregate Weekly Payrolls of All Employees, Total Private", "Index 2007=100"],
        "TLNRESCONS" : ["TotalConstructionSpending","Total Construction Spending: Nonresidential in the United States","Millions of Dollars"],
        "PNRESCONS" : ["PrivateConstructionSpending","Total Private Construction Spending: Nonresidential in the United States", "Millions of Dollars"],
        "PBNRESCONS": ["PublicConstructionSpending","Total Public Construction Spending: Nonresidential in the United States", "Millions of Dollars"],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        "": ["","",""],
        
        
        }

        for index in self.macro_indices: # Note: self.indices is a tuple with a single list
            print(f"Fetching {index}...")
            series = fred.get_series(index, self.start_day, self.end_day)
            series = series.resample("D").ffill().reset_index()
            series.columns = ["date", 'FRED_'+names[index][0]]
            dfs.append(series)

        # Merge all dataframes on 'date'
        macro_df = dfs[0]
        for df in dfs[1:]:
            macro_df = macro_df.merge(df, on='date', how='outer')

        # Rename the columns
        macro_df.rename(columns=names, inplace=True)

        macro_df = macro_df.round(4)
        macro_df.to_csv('fred_macro_time_series.csv', index=False)

        sereis_list = [['FRED_' + value[0], value[1], value[2]] for value in names.values()]
        fred_ref = pd.DataFrame(sereis_list, columns=['Data Series', 'Description', 'Unit'])
        fred_ref['Source'] = 'FRED'
        fred_ref['Category'] = 'Macro'

        fred_ref.to_csv('fred_macro_reference.csv', index=False)

        print('fred macro data created')
        return macro_df

    def fetch_steel_data(self):
        fred = Fred(api_key=self.api_keys["Fred"])
        dfs = []

        # Mapping of series IDs to their actual names
        # value contains the list [Index, Description, Unit, Category]
        names = {
            "PIORECRUSDM": ["GlobalIronOrePrice", "Global price of Iron Ore", "U.S. Dollars per Metric Ton", "Commodity Price"],
            "PCU2123122123120": ["Limestone", "Crushed and Broken Limestone", "Index Dec 1983=100", "Commodity Price"],
            "IPG3311A2NQ": ["IronSteelProducts", "US Iron Steel Products", "Index 2017=100", "Steel Supply & Demand"],
            "WPU101707": ["PPIColdRolledSteel", "PPI by Commodity: Metals and Metal Products: Cold Rolled Steel Sheet and Strip", "Index Jun 1982=100", "Steel Supply & Demand"],
            "WPU10170502": ["PPISteelWireStainlessSteel", "PPI by Commodity: Metals and Metal Products: Steel Wire, Stainless Steel", "Index Dec 2010=100", "Steel Supply & Demand"],
            "WPU101": ["PPIIronSteel", "PPI by Commodity: Metals and Metal Products: Iron and Steel", "Index 1982=100", "Steel Supply & Demand"],
            "A31ANO": ["SteelManufacturersNewOrders", "Manufacturers' New Orders: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing", "Millions of Dollars", "Steel Supply & Demand"],
            "IPN3311A2RS": ["IndustrialProductionRawSteel", "Industrial Production: Manufacturing: Durable Goods: Raw Steel", "Index 2017=100", "Steel Supply & Demand"]
        }

        for index in self.steel_indices: # Note: self.indices is a tuple with a single list
            print(f"Fetching {index}...")
            series = fred.get_series(index, self.start_day, self.end_day)
            series = series.resample("D").ffill().reset_index()
            series.columns = ["date", 'FRED_'+names[index][0]]
            dfs.append(series)

        # Merge all dataframes on 'date'
        macro_df = dfs[0]
        for df in dfs[1:]:
            macro_df = macro_df.merge(df, on='date', how='outer')

        # Rename the columns
        macro_df.rename(columns=names, inplace=True)

        macro_df = macro_df.round(4)
        macro_df.to_csv('fred_steel_time_series.csv', index=False)

        sereis_list = [['FRED_' + value[0], value[1], value[2], value[3]] for value in names.values()]
        fred_ref = pd.DataFrame(sereis_list, columns=['Data Series', 'Description', 'Unit', 'Category'])
        fred_ref['Source'] = 'FRED'

        fred_ref.to_csv('fred_steel_reference.csv', index=False)

        print('fred steel data created')
        return macro_df