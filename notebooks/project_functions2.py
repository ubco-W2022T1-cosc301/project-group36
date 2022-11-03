import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    import pandas as pd
    import numpy as np
    #Method Chain
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(["Last Updated","Current Ver","Android Ver"],axis=1)
        .dropna()
        .reset_index()
        .drop_duplicates(subset=['App'],inplace=True)
        .rename(columns = {'App':'App Name', 'Price':'Price_USD','Size':'Size_MB'})
        )
    df1['Installs'] = df1['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else x)
    df1['Installs'] = df1['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else x)
    df1['Installs'] = df1['Installs'].astype(float)
    df1['Size_MB'] = df1['Size_MB'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
    df1['Size_MB'] = df1['Size_MB'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
    df1['Size_MB'] = df1['Size_MB'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    df1['Size_MB'] = df1['Size_MB'].astype(float)
    df1['Price_USD'] = df1['Price_USD'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else x)
    df1['Price_USD'] = df1['Price_USD'].astype(float)                
    
    return df1