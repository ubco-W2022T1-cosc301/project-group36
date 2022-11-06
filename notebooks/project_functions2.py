import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(url_or_path_to_csv_file):
    #Method Chain
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(["Last Updated","Current Ver","Android Ver"],axis=1)
        .dropna()
        .reset_index()
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
    
    df2 = (df1
            .assign(Rating_Dist = np.select([df1.Rating > 4.4,df1.Rating > 3.9,df1.Rating > 3.4,df1.Rating > 2.9,df1.Rating > 2.4 ]
                               , ['Above 4.5', "4 - 4.5",'3.5 - 4', "3 - 3.5", "2.5 - 3"], "Less Than 2.5"))
            .assign(Size_MB_Dist = np.select([df1.Size_MB < 21,df1.Size_MB < 41
                                              ,df1.Size_MB < 61,df1.Size_MB < 81,df1.Size_MB < 101]
                              , ['0 - 20 MB', "20 - 40 MB",'40 - 60 MB', "60 - 80 MB", "80 - 100 MB"])))
            
    
    return df2