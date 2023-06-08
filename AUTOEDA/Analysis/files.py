from utils import *

class Load_Dataset():
    
    def __init__(self):
        
        print("Loading Dataset")

    ##csv sheets
    def read_csv(self,data):
        self.df = pd.read_csv(data)
        return self.df
    
    #excel sheets
    def read_excel(self,data):
        self.df = pd.read_excel(data)
        return self.df
    
     #txt files
    def read_txt(self, file_path):
        self.df = pd.read_csv(file_path, delimiter='\t')
        return self.df  
    
    #json files
    # Get the data as a string.
     # Load the data from the JSON string.
     # If the data is not a dictionary, convert it to a dictionary.
     # Create a DataFrame from the data dictionary.
    def read_json(self,data):
       
        data_str = data.read()
     
        data_dict = json.loads(data_str)
        
        if not isinstance(data_dict, dict):
            data_dict = {'data': data_dict}
        
       
        self.df = pd.DataFrame(data_dict)
        if len(self.df.columns) == 1:
            self.df.reset_index(inplace=True)

        return self.df
    
   

