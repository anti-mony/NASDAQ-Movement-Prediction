import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def split_data(file_path = None, df = None, prefix="", seed=1, ret = 0):
    
    """
    Splits data into Train, Test and Validation and saves them in the ProcessedData folder
    
    Args:
        file_path: Input Data in csv format
        df: Dataframe can be sent instead of a file
        prefix: Prefix for file names like:
            [Prefix]_train.csv, [Prefix]_test.csv, [Prefix]_val.csv
        seed: seed to randomize the split
        ret: set to 1 if you want the data_frames_back as well 
    
    Returns:
        Tuple of Train, Val and Test pandas dataframes.
    """
    
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
    
    if ret == 1:
        return train, val, test