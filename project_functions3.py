import pandas as pd
import numpy as np
import seaborn as sb

# We had asked the prof and he said we could use these steps because we could not convert
#some steps properly

#Method Chain 1
df = (
    pd.read_csv('../data/raw/google_play_store.csv')
    .drop(["Price", "Category","Current Ver","Android Ver", "Last Updated"],axis=1)
    .dropna()
    .reset_index()
)

df['Size'] = df['Size'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
df['Size'] = df['Size'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
df['Size'] = df['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
df['Size'] = df['Size'].astype(float)
df['Reviews'] = df['Reviews'].astype(float)

#Method Chain 2
df1 = (
    df
    .rename(columns = {'Size':'Size MB'})
    .rename(columns = {'Reviews':'No. of reviews'})
)

df1['Installs'] = df1['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else x)
df1['Installs'] = df1['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else x)
df1['Installs'] = df1['Installs'].astype(float)
indexName = df1[ (df1['Rating'] < 1) & (df1['Rating'] > 5) ].index

#Method Chain 3
df2 = (
    df1
)

df2 = df2.rename(columns = {'Installs':'Downloads'})
df2 = df2.drop(indexName)
df2 = df2.rename(columns = {'Content Rating':'Audience'})
df2 = df2.reset_index()
df2.head()