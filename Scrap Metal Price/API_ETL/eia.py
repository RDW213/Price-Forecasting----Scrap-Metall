import pandas as pd
eia_data_list = []

class Eia(): 
    def __init__(self):
        pass

    @staticmethod
    def fetch_energy_climate_data():
        # Coal
        # eia coal Monthly Energy Review
        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T06.01'

        try:
            df = pd.read_csv(url)
        except Exception as e:
            print(f"An error occurred: {e}")

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df['Category'] = 'Energy'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Category', 'Source','Unit', 'Date', 'Value']]
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Data Series'] = 'US ' + df['Data Series']
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        eia_coal = df.reset_index(drop=True)
        eia_data_list.append(eia_coal)

        # Energy in general
        # eia Monthly Primary energy overview
        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T01.01'

        try:
            df = pd.read_csv(url)
        except Exception as e:
            print(f"An error occurred: {e}")

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df['Category'] = 'Energy'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Category', 'Source','Unit', 'Date', 'Value']]
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Data Series'] = 'US ' + df['Data Series']
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        eia_primary_energy = df.reset_index(drop=True)
        eia_data_list.append(eia_primary_energy)

        # Heating Degree-Days
        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T01.10'

        try:
            df = pd.read_csv(url)
        except Exception as e:
            print(f"An error occurred: {e}")

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df['Category'] = 'Energy'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Category', 'Source','Unit', 'Date', 'Value']]
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        eia_Heating_degree_days = df.reset_index(drop=True)
        eia_data_list.append(eia_Heating_degree_days)

        # Cooling Degree-Days
        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T01.11'

        try:
            df = pd.read_csv(url)
        except Exception as e:
            print(f"An error occurred: {e}")

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df['Category'] = 'Energy'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Category', 'Source','Unit', 'Date', 'Value']]
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        eia_cooling_degree_days = df.reset_index(drop=True)
        eia_data_list.append(eia_cooling_degree_days)

        # Natural Gas

        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T04.01'

        df = pd.read_csv(url)

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df['Category'] = 'Energy'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Category', 'Source','Unit', 'Date', 'Value']]
        df['Data Series'] = 'US ' + df['Data Series']
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        eia_natural_gas = df.reset_index(drop=True)
        eia_data_list.append(eia_natural_gas)

        # Crude Oil
        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T03.01'

        df = pd.read_csv(url)

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df['Category'] = 'Energy'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Category', 'Source','Unit', 'Date', 'Value']]
        df['Data Series'] = 'US ' + df['Data Series']
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        Petroleum = df.reset_index(drop=True)
        eia_data_list.append(Petroleum)

        # Electricity 
        url = 'https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T07.01'
        df = pd.read_csv(url)

        df = df[df['YYYYMM'] % 100 <= 12]
        df['Date'] = pd.to_datetime(df['YYYYMM'].astype(str), format='%Y%m')
        df['Source'] = 'EIA'
        df.rename(columns={'Description': 'Data Series'}, inplace=True)
        df = df[['Data Series', 'Source','Unit', 'Date', 'Value']]
        df['Data Series'] = 'US ' + df['Data Series']
        df['Unit'] = df['Unit'].replace('Thousand Short Tons', '1000 ST')
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        Electricity = df.reset_index(drop=True)
        eia_data_list.append(Electricity)

        # Combination
        # Vertically concatenate the DataFrames
        joined_df = pd.concat(eia_data_list, axis=0, ignore_index=True)
        joined_df['Category'] = joined_df['Data Series'].apply(lambda x: 'Climate' if 'Heating' in x or 'Cooling' in x else 'Energy')
        joined_df['Data Series'] = joined_df['Data Series'].str.replace('"', "")

        # Export the resulting DataFrame to a CSV file
        # joined_df.to_csv('eia_energy_data.csv', index=False)

        #----------------------------------------------------Below is the reformation----------------------------------------------------------

        # df = pd.read_csv('eia_energy_data.csv')
        df = joined_df
        df['Data Series'] = df['Data Series'].str.replace('"', "")
        df['Data Series'] = df['Data Series'].str.replace(",", "")
        df['Data Series'] = df['Data Series'].str.replace(" ", "_")
        df['Data Series'] = "EIA_" + df['Data Series']

        series_list = df['Data Series'].unique()

        ts = df[df['Data Series'] == series_list[0]][['Date', 'Value']].rename(columns={'Value': series_list[0]})

        for series in series_list[1:]:
            series_df = df[df['Data Series'] == series][['Date', 'Value']].rename(columns={'Value': series})
            print(series_df.head())
            ts = pd.merge(ts, series_df, on='Date', how='outer')

        ts.to_csv('eia_time_series.csv', index=False)

        ref = df[['Data Series', 'Category', 'Source', 'Unit']].drop_duplicates()


        ref['Description'] = None
        ref.to_csv('eia_reference.csv', index=False)

