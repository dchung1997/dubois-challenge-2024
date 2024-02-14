import pandas as pd

variable_year = [
    'occ18501900.tsv',
    'occ19101920.tsv',
    'occ1930.tsv',
    'occ1940.tsv',
    'occ1950.tsv',
    'occ1960.tsv'
]

df_arr = []

for s in variable_year :
    df_arr.append(pd.read_csv('./data/' + s, sep='\t', index_col=False))

historical_df = pd.read_csv("./data/output.csv", index_col=False);

for index, row in historical_df.iterrows():
    year = int(row['YEAR'])
    if  1900 >= year:
        result = df_arr[0].loc[df_arr[0]['OCC'] == row['OCC']]
    elif 1920 >= year >= 1910:
        result = df_arr[1].loc[df_arr[1]['OCC'] == row['OCC']]
    elif year == 1930:
        result = df_arr[2].loc[df_arr[2]['OCC'] == row['OCC']]
    elif year == 1940:
        result = df_arr[3].loc[df_arr[3]['OCC'] == row['OCC']]
    elif year == 1950:
        result = df_arr[4].loc[df_arr[4]['OCC'] == row['OCC']]
    elif year == 1960:
        result = df_arr[5].loc[df_arr[5]['OCC'] == row['OCC']]
    
    print(str(index) + " " + result['Occupation'].iloc[0])
    historical_df.loc[index, 'Occupation'] = result['Occupation'].iloc[0]  

historical_df = historical_df[historical_df['OCC'] != 999]

historical_df.to_csv('./data/output_occupations.csv', index=False) 
