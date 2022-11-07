import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.read_csv('../data/raw/google_play_store.csv')
        .drop(["Last Updated","Current Ver","Android Ver"],axis=1)
        .dropna()
        .reset_index()
        .rename(columns = {'App':'App Name', 'Size':'Size (MB)', 'Price':'Price ($)'})
    )
    # Note: The professor has allowed us to do these below steps seperately.
    df['Installs'] = df['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else x)
    df['Installs'] = df['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else x)
    df['Installs'] = df['Installs'].astype(float)
    df['Size (MB)'] = df['Size (MB)'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
    df['Size (MB)'] = df['Size (MB)'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
    df['Size (MB)'] = df['Size (MB)'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    df['Size (MB)'] = df['Size (MB)'].astype(float)
    df['Price ($)'] = df['Price ($)'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else x)
    df['Price ($)'] = df['Price ($)'].astype(float)
    df['Reviews'] = df['Reviews'].astype(float)
    
    return df