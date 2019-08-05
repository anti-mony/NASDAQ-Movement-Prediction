import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def split_data(file_path = None, df = None, prefix="", seed=1):
    
    if file_path is not None:
        data = pd.read_csv(file_path)
        data.drop(columns=['Unnamed: 0'], inplace = True)
    elif df is not None:
        data = df
    else:
        print("Error : Please Provide a Datafile/Frame")
    
    train, test = train_test_split(data, test_size=0.3, random_state=seed)
    train, val = train_test_split(train, test_size=0.3, random_state=seed)
    
    dir_prefix = 'ProcessedData/'
    
    train.to_csv(dir_prefix+prefix+"_train.csv", index=False, header=False)
    val.to_csv(dir_prefix+prefix+"_val.csv", index=False, header=False)
    test.to_csv(dir_prefix+prefix+"_test.csv", index=False, header=False)