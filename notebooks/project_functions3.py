import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_and_process(url_or_path_to_csv_file):
    #Method Chain 1
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(["Price","Current Ver","Android Ver", "Last Updated"],axis=1)
        .dropna()
        .reset_index()
        .rename(columns = {'Size':'Size MB','Reviews':'No. of reviews','Installs':'Downloads','Content Rating':'Audience'})
        )
    # We had asked the prof and he said we could do the below steps seperately.
    df['Size MB'] = df['Size MB'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
    df['Size MB'] = df['Size MB'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
    df['Size MB'] = df['Size MB'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    df['Size MB'] = df['Size MB'].astype(float)
    df['No. of reviews'] = df['No. of reviews'].astype(float)
    df['Downloads'] = df['Downloads'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else x)
    df['Downloads'] = df['Downloads'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else x)
    df['Downloads'] = df['Downloads'].astype(float)
    indexName = df[ (df['Rating'] < 1) & (df['Rating'] > 5) ].index
    indexName = df[ (df['Rating'] < 1) & (df['Rating'] > 5) ].index
    df.drop(indexName , inplace=True)
    
    return df