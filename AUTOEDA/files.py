from utils import *


## Define a class to open and read the file
class DataFrame_Loader():

    
    def __init__(self):
        
        print("Loading DataFrame")
    
    ##csv dataset
    def read_csv(self,data):
        self.df = pd.read_csv(data)
        return self.df
    
    #xlsx dataset
    def read_excel(self,data):
        self.df = pd.read_excel(data)
        return self.df
    
    #json dataset
    def read_excel(self,data):
        self.df = pd.read_json(data)
        return self.df
    
    
    