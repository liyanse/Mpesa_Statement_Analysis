from utils import *

## Define a class to open and read the csv file
class Data_Loader():
    
    def __init__(self):
        print("Loading Dataset")
        
    def read_csv(self, data):
        self.df = pd.read_csv(data)
        return self.df
    

class Data_Analysis():
    def __init__(self):
        print("General Descriptive Analysis")
    
    def data_types(self,x):
        return x.dtypes
    
    def null_values(self, x):
        return x.isna().sum()
    
    def null1_values(self, x):
        return x.isna().sum()
    
    def null2_values(self, x):
          return x.isna().sum()
      
    def hist(self,x):
        return x.hist()
    
    def Tabulation(self, x):
        table = pd.DataFrame(x.dtypes, columns=['dtypes'])
        table1  =pd.DataFrame(x.coli,ms, columns=['Names'])
        table = table.reset_index()
        table =table.rename(columns={'index':'Names'})
        table['No of Missing'] = x.isnull().sum().values
        table['No of Uniques'] = x.nunique().values
	    table['Percent of Missing'] = ((x.isnull().sum().values)/ (x.shape[0])) *100
	    table['First Observation'] = x.loc[0].values
	    table['Second Observation'] = x.loc[1].values
	    table['Third Observation'] = x.loc[2].values
	    for name in table['Name'].value_counts().index:
	        table.loc[table['Name'] == name, 'Entropy'] = round(stats.entropy(x[name].value_counts(normalize=True), base=2),2)
	    return table
 
    def Numerical_variables(self,x):
	    Num_var = [var for var in x.columns if x[var].dtypes!="object"]
	    Num_var = x[Num_var]
	    return Num_var

    def categorical_variables(self,x):
	    cat_var = [var for var in x.columns if x[var].dtypes=="object"]
	    cat_var = x[cat_var]
	    return cat_var

    def impute(self,x):
	    df=x.dropna()
	    return df

    def imputee(self,x):
	    df=x.dropna()
	    return df

    def Show_pearsonr(self,x,y):
	    result = pearsonr(x,y)
	    return result

	
    def Show_spearmanr(self,x,y):
	    result = spearmanr(x,y)
	    return result


    def plotly(self,a,x,y):
	    fig = px.scatter(a, x=x, y=y)
	    fig.update_traces(marker=dict(size=10,
	                                  line=dict(width=2,
	                                            color='DarkSlateGrey')),
	                      selector=dict(mode='markers'))
	    fig.show()

    def show_displot(self,x):
	        plt.figure(1)
	        plt.subplot(121)
	        sns.distplot(x)
         
         plt.subplot(122)
         x.plot.box(figsize=(16,5))
         
         plt.show()
        
        
    
        