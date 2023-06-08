from utils import *

   
    #Method to read the dataset 
def load_dataset(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.json'):
        return pd.read_parquet(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)

