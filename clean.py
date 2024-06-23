import pandas as pd
df = pd.read_csv('data/ten_year.csv')
df['date'] = pd.to_datetime(df['update'],format='%d/%m/%Y %H:%M:%S').dt.date
df = df.drop(columns='update')
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)
df = df.drop_duplicates()
df.to_csv('data/ten_year.csv')