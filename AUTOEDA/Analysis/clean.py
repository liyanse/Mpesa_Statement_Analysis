from utils import *
from files import *

class Understand_Datafame():
    
    """
        In this class; we'll be handling the basic steps we take to clean and understand out dataset
        That is, understanding shape, ifno, descripbe, null values, columns, dropna, removing duplicates, and filling null values
        
    """
    
    def __init__(self):
        
        print("Created Cleaning Object")
    
    #shape
    def show_shape(self,x):
        
        return x.shape
    
    #dtypes
    def show_dtypes(self,x):
        
        return x.dtypes
    
    def show_desc(self, x):
    
        return x.describe().drop('count', axis=1)
    
    #columns
    def show_columns(self,x):
        
        return x.columns
    
 
 
class Attribute_Information():

    def Column_information(self,data):
    
        data_info = pd.DataFrame(
                                columns=['No of observations',
                                        'No of Variables',
                                        'No of Numerical Variables',
                                        'No of Factor Variables',
                                        'No of Categorical Variables',
                                        'No of Logical Variables',
                                        'No of Date Variables',
                                        'No of zero variance variables'])


        data_info.loc[0,'No of observations'] = data.shape[0]
        data_info.loc[0,'No of Variables'] = data.shape[1]
        data_info.loc[0,'No of Numerical Variables'] = data._get_numeric_data().shape[1]
        data_info.loc[0,'No of Factor Variables'] = data.select_dtypes(include='category').shape[1]
        data_info.loc[0,'No of Logical Variables'] = data.select_dtypes(include='bool').shape[1]
        data_info.loc[0,'No of Categorical Variables'] = data.select_dtypes(include='object').shape[1]
        data_info.loc[0,'No of Date Variables'] = data.select_dtypes(include='datetime64').shape[1]
        data_info.loc[0,'No of zero variance variables'] = data.loc[:,data.apply(pd.Series.nunique)==1].shape[1]

        data_info =data_info.transpose()
        data_info.columns=['value']
        data_info['value'] = data_info['value'].astype(int)


        return data_info
        
    def __iqr(self,x):
        return x.quantile(q=0.75) - x.quantile(q=0.25)

    def __outlier_count(self,x):
        upper_out = x.quantile(q=0.75) + 1.5 * self.__iqr(x)
        lower_out = x.quantile(q=0.25) - 1.5 * self.__iqr(x)
        return len(x[x > upper_out]) + len(x[x < lower_out])

    def num_count_summary(self,df):
        df_num = df._get_numeric_data()
        data_info_num = pd.DataFrame()
        i=0
        for c in  df_num.columns:
            data_info_num.loc[c,'Negative values count']= df_num[df_num[c]<0].shape[0]
            data_info_num.loc[c,'Positive values count']= df_num[df_num[c]>0].shape[0]
            data_info_num.loc[c,'Zero count']= df_num[df_num[c]==0].shape[0]
            data_info_num.loc[c,'Unique count']= len(df_num[c].unique())
            data_info_num.loc[c,'Negative Infinity count']= df_num[df_num[c]== -np.inf].shape[0]
            data_info_num.loc[c,'Positive Infinity count']= df_num[df_num[c]== np.inf].shape[0]
            data_info_num.loc[c,'Missing Percentage']= df_num[df_num[c].isnull()].shape[0]/ df_num.shape[0]
            data_info_num.loc[c,'Count of outliers']= self.__outlier_count(df_num[c])
            i = i+1
        return data_info_num
    
    def statistical_summary(self,df):
    
        df_num = df._get_numeric_data()

        data_stat_num = pd.DataFrame()

        try:
            data_stat_num = pd.concat([df_num.describe().transpose(),
                                       pd.DataFrame(df_num.quantile(q=0.10)),
                                       pd.DataFrame(df_num.quantile(q=0.90)),
                                       pd.DataFrame(df_num.quantile(q=0.95))],axis=1)
            data_stat_num.columns = ['count','mean','std','min','25%','50%','75%','max','10%','90%','95%']
        except:
            pass

        return data_stat_num
 
class Clean_Dataframe():
    
    #Show duplicates values
    def get_duplicate_values(self,data):
        
        duplicated_values = data.duplicated()
        
        return duplicated_values
    
    #Show duplicates values
    def fill_duplicate_values(self,data):
        
        drop_duplicates = data.drop_duplicates()
        
        return drop_duplicates
    
    #null values
    def get_missing_values(self,data):
        
        missing_values = data.isnull().sum()
        missing_values.sort_values(ascending=False, inplace=True)
        return missing_values
    
    #drop null values
    def drop_missing_values(self,data):
        
        drop_values = data.dropna()
        return drop_values
    
    #fill null values
    def fill_missing_values(self, data):

        # Fill null values with mean
        data = data.fillna(data.mean())

        # Save the changes
        data.fillna(data.mean(), inplace=True)

        return data
