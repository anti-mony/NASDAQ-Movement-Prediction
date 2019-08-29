NASDAQ-Movement-Prediction
=====
`Predicting Nasdaq Movement Prediction according to each new article.` 

### Execution

Just upload the entire repo as is and run a jupyter server. And execute the notebook, after the pre-processing section.

### Directory Structure:

##### Some basic info:
* All the scripts are stored in the root directory.
* All data files are in folders such as RawData, ProcessedData and Embeddings

##### Structure

* **Embeddings** (Folder): Stores the GLOVE Embeddings 
* **RawData** (Folder): Stores all the un-processed financial and news data 
* **ProcessedData** (Folder): This folder contains all the processed data in form. 
    > The repository only contains a small portion of the dataset which is pre-processed already. Also split into test, train and validation so that it's easy to ingest. 

* __pre_pre_process_data.py__ : This is the first stage of processing the data. Completely raw data is read in and data formats are changed and the overlapping data from market and news (date-wise) stored.

* __combine_data.py__ : This script reads in the market and news data outputed by the script above and combines the two according to the dates and also makes the market data from minute wise to each day.

* __split_data.py__ : This script splits a data frame into test, train and validation data and stores it to the disk. 

* **MainColab.ipynb** : This Notebook contains all the MachineLearning and some pre-processing. This contains the run results from Google Colab.

* **Main.ipynb**: Same file as above, just wothout any run results.

