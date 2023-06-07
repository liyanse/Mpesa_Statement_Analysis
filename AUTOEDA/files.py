from utils import *
   
## Define a class to open and read the file
class DataFrame_Loader():

    
    def __init__(self):
        
        print("Loading DataFrame")
    
    def read_excel(self,data):
        if data.endswith(".xlsx") or data.endswith(".xls"):
            self.df = pd.read_excel(data, encoding="Windows-1252")
            return self.df
        
    ##csv dataset
    def read_csv(self,data):
        self.df = pd.read_csv(data)
        return self.df
    
     #json dataset
    def read_json(self,data):
        self.df = pd.read_json(data)
        return self.df
    
    #txt dataset
    def read_txt(self, file_path):
        self.df = pd.read_csv(file_path, delimiter='\t')
        return self.df
        
