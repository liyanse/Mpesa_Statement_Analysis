from utils import *
from files import *

class Data_Preprocess():
    
    def __init__(self):
        print("Intialized Data Preprocessing")
        
    #Method to Explore  the dataset
    def explore_dataset(data):
        """Provides summary statistics and visualizations of the dataset."""
    #Dataset Shape
        print("Dataset shape:", data.shape)

    #Check the dataset  columns datatype
        print("Dataset data types:\n", data.dtypes)

    #Check for the missing values
        print("Number of missing values:\n", data.isna().sum())
    
    #Check the columns i the dataset
        print("The columns include:\n", data.columns)
    
    #load_dataset
    data = load_dataset('survey.csv')
    
    #explore_dataset(data)
    
    def clean_dataset(data):
    #Remove duplicates    
        data.drop_duplicates(inplace=True)
        
    ##Fill missing values
        data.fillna(method="ffill", inplace=True)
        
    ##Drop columns with a high percentage of missing values
        missing_percent = data.isnull().sum()/len(data)*100
        to_drop = list(missing_percent[missing_percent>50].index)
        data.drop(to_drop, axis=1, inplace=True)
        
        if to_drop:
            data.dropna(inplace=True)
        return data
    
    clean_dataset(data)
            