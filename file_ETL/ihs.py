import os
import pandas as pd

current_directory = os.getcwd()
file_list = os.listdir(current_directory)
csv_files = [file for file in file_list if file.endswith('.csv')]
csv_files = [file for file in csv_files if file not in ['ihs_reference.csv', 'ihs_time_series.csv']]

# use ts_list to store all the ts data extracted from csv files
ts_list = []
ref = { 'Data Series': [], 
        'Description': [],
        'Unit': [],
        'Category': [],
        'Source': []}
description_col_map = dict()
for csv_file in csv_files:
    file_path = os.path.join(current_directory, csv_file)
    df = pd.read_csv(file_path)
    df = df.rename(columns={'Period': 'Date', 
                                       'Concept': 'Category', 
                                       'Short Label': 'Description',
                                       'Unit' : 'Category'})
    descriptions = df['Description'].unique().tolist()
    for description in descriptions:
        column_name = description.replace(',' , '').replace("Standard & Poors ", 'SP').replace('United States', 'US')\
                                 .replace('- ','').replace('U.S.','').replace('(','').replace(')','').replace('.','').replace(' ', '_').replace('__', '_')
        column_name = 'ihs_' + column_name
        # key is the description, value is the column_name(Data Series)
        description_col_map[description] = column_name

    for key, value in description_col_map.items():
        ts = df[df['Description'] == key][['Date', 'Value']].rename(columns = {'Value': value}) 
        ts_list.append(ts)
        ref['Data Series'].append(value)
        ref['Description'].append(key)
        ref['Unit'].append('')
        try:
            ref['Category'].append(df[df['Description'] == key].iloc[0]['Category'])
        except:
            ref['Category'].append('')
        ref['Source'].append('ihs')

# some csv files contain same data series, and we wanna keep the longer one
data_series_dict = {}

for idx, df in enumerate(ts_list):
    for column in df.columns:
        if column != 'Date':
            non_null_count = df[column].count()
            if column not in data_series_dict or non_null_count > data_series_dict[column][0]:
                data_series_dict[column] = (non_null_count, idx)

_, initial_idx = max(data_series_dict.values())
ts = ts_list[initial_idx]

for column, (_, idx) in data_series_dict.items():
    if idx != initial_idx:
        ts = pd.merge(ts, ts_list[idx], on='Date', how='outer')

ts.to_csv('../ihs_time_series.csv', index=False)

ref = pd.DataFrame(ref)
ref = ref.drop_duplicates()
ref = ref[~(ref.duplicated(subset='Data Series') & ref['Category'].isna())]
ref.to_csv('../ihs_reference.csv', index=False)