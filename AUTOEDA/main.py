from utils import *

## Define a class to open and read the csv file
class DataFrame_Loader():

    
    def __init__(self):
        
        print("Loading DataFrame")
        
    def read_csv(self,data):
        self.df = pd.read_csv(data)
        return self.df

class EDA_Dataframe_Analysis():

    
    def __init__(self):
        
        print("General_EDA object created")

    def show_dtypes(self,x):
    	return x.dtypes


    def show_columns(self,x):
    	return x.columns


    def Show_Missing(self,x):
    	return x.isna().sum()


    def Show_Missing1(self,x):
	    return x.isna().sum()


    def Show_Missing2(self,x):
	    return x.isna().sum()


    def show_hist(self,x):
    	return x.hist()


    def Tabulation(self,x):
	    table = pd.DataFrame(x.dtypes,columns=['dtypes'])
	    table1 =pd.DataFrame(x.columns,columns=['Names'])
	    table = table.reset_index()
	    table= table.rename(columns={'index':'Name'})
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

    def Show_DisPlot(self,x):
	    plt.style.use('fivethirtyeight')
	    plt.figure(figsize=(12,7))
	    return sns.distplot(x, bins = 25)

    def Show_CountPlot(self,x):
	    fig_dims = (18, 8)
	    fig, ax = plt.subplots(figsize=fig_dims)
	    return sns.countplot(x,ax=ax)

    def plotly_histogram(self,a,x,y):
	    fig = px.histogram(a, x=x, y=y)
	    fig.update_traces(marker=dict(size=10,
	                                  line=dict(width=2,
	                                            color='DarkSlateGrey')),
	                      selector=dict(mode='markers'))
	    fig.show()


    def plotly_violin(self,a,x,y):
	    fig = px.histogram(a, x=x, y=y)
	    fig.update_traces(marker=dict(size=10,
	                                  line=dict(width=2,
	                                            color='DarkSlateGrey')),
	                      selector=dict(mode='markers'))
	    fig.show()

    def Show_PairPlot(self,x):
	    return sns.pairplot(x)

    def Show_HeatMap(self,x):
	    f,ax = plt.subplots(figsize=(15, 15))
	    return sns.heatmap(x.corr(),annot=True,ax=ax);

    def wordcloud(self,x):
	    wordcloud = WordCloud(width = 1000, height = 500).generate(" ".join(x))
	    plt.imshow(wordcloud)
	    plt.axis("off")
	    return wordcloud

    def label(self,x):
	    from sklearn.preprocessing import LabelEncoder
	    le = LabelEncoder()
	    x=le.fit_transform(x)
	    return x

    def label1(self,x):
	    from sklearn.preprocessing import LabelEncoder
	    le = LabelEncoder()
	    x=le.fit_transform(x)
	    return x
   
    def concat(self,x,y,z,axis):
    	return pd.concat([x,y,z],axis)

    def dummy(self,x):
    	return pd.get_dummies(x)


    def qqplot(self,x):
    	return sm.qqplot(x, line ='45')


    def Anderson_test(self,a):
    	return anderson(a)

    def PCA(self,x):
	    pca =PCA(n_components=8)
	    principlecomponents = pca.fit_transform(x)
	    principledf = pd.DataFrame(data = principlecomponents)
	    return principledf

    def outlier(self,x):
	    high=0
	    q1 = x.quantile(.25)
	    q3 = x.quantile(.75)
	    iqr = q3-q1
	    low = q1-1.5*iqr
	    high += q3+1.5*iqr
	    outlier = (x.loc[(x < low) | (x > high)])
	    return(outlier)



    def check_cat_relation(self,x,y,confidence_interval):
	    cross_table = pd.crosstab(x,y,margins=True)
	    stat,p,dof,expected = chi2_contingency(cross_table)
	    print("Chi_Square Value = {0}".format(stat))
	    print("P-Value = {0}".format(p))
	    alpha = 1 - confidence_interval
	    return p,alpha
	    if p > alpha:
	        print(">> Accepting Null Hypothesis <<")
	        print("There is no relationship between the two variables")
	    else:
	        print(">> Rejecting Null Hypothesis <<")
	        print("There is a significant relationship between the two variables")



class Attribute_Information():

    def __init__(self):
        
        print("Attribute Information object created")
        
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

    def __get_missing_values(self,data):
        
        #Getting sum of missing values for each feature
        missing_values = data.isnull().sum()
        #Feature missing values are sorted from few to many
        missing_values.sort_values(ascending=False, inplace=True)
        
        #Returning missing values
        return missing_values

        
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



class Data_Base_Modelling():

    
    def __init__(self):
        
        print("Begin General Explaratory Analysis")


    def Label_Encoding(self,x):
	    category_col =[var for var in x.columns if x[var].dtypes =="object"] 
	    labelEncoder = preprocessing.LabelEncoder()
	    mapping_dict={}
	    for col in category_col:
	        x[col] = labelEncoder.fit_transform(x[col])
	        le_name_mapping = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
	        mapping_dict[col]=le_name_mapping
	    return mapping_dict

    def IMpupter(self,x):
	    imp_mean = IterativeImputer(random_state=0)
	    x = imp_mean.fit_transform(x)
	    x = pd.DataFrame(x)
	    return x


    def Logistic_Regression(self,x_train,y_train,x_test,y_test):
    	pipeline_dt=Pipeline([('dt_classifier',LogisticRegression())])
    	pipelines = [pipeline_dt]
    	best_accuracy=0.0
    	best_classifier=0
    	best_pipeline=""
    	pipe_dict = { 0: 'Decision Tree'}
    	for pipe in pipelines:
    		pipe.fit(x_train, y_train)
    	for i,model in enumerate(pipelines):
    		return (classification_report(y_test,model.predict(x_test)))


    def Decision_Tree(self,x_train,y_train,x_test,y_test):
    	pipeline_dt=Pipeline([('dt_classifier',DecisionTreeClassifier())])
    	pipelines = [pipeline_dt]
    	best_accuracy=0.0
    	best_classifier=0
    	best_pipeline=""
    	pipe_dict = { 0: 'Decision Tree'}
    	for pipe in pipelines:
    		pipe.fit(x_train, y_train)
    	for i,model in enumerate(pipelines):
    		return (classification_report(y_test,model.predict(x_test)))

    def RandomForest(self,x_train,y_train,x_test,y_test):
    	pipeline_dt=Pipeline([('dt_classifier',RandomForestClassifier())])
    	pipelines = [pipeline_dt]
    	best_accuracy=0.0
    	best_classifier=0
    	best_pipeline=""
    	pipe_dict = { 0: 'Decision Tree'}
    	for pipe in pipelines:
    		pipe.fit(x_train, y_train)
    	for i,model in enumerate(pipelines):
    		return (classification_report(y_test,model.predict(x_test)))

    def naive_bayes(self,x_train,y_train,x_test,y_test):
    	pipeline_dt=Pipeline([('dt_classifier',GaussianNB())])
    	pipelines = [pipeline_dt]
    	best_accuracy=0.0
    	best_classifier=0
    	best_pipeline=""
    	pipe_dict = { 0: 'Decision Tree'}
    	for pipe in pipelines:
    		pipe.fit(x_train, y_train)
    	for i,model in enumerate(pipelines):
    		return (classification_report(y_test,model.predict(x_test)))

    def XGb_classifier(self,x_train,y_train,x_test,y_test):
    	pipeline_dt=Pipeline([('dt_classifier',XGBClassifier())])
    	pipelines = [pipeline_dt]
    	best_accuracy=0.0
    	best_classifier=0
    	best_pipeline=""
    	pipe_dict = { 0: 'Decision Tree'}
    	for pipe in pipelines:
    		pipe.fit(x_train, y_train)
    	for i,model in enumerate(pipelines):
    		return (classification_report(y_test,model.predict(x_test)))
