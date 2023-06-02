from utils import *
from main import *

def main():
	st.title("Automated Explaratory Data Analysis")
	
	st.markdown(' Select service from the service menus, we offer services such as;')
 
	st.markdown('**1. EDA  -** Exploratory data analysis is a way of looking at data to learn more about it.')
	st.markdown('**2. Visualizations For Linear Models -** Visualizations for linear models are like maps that help us see how two things are related.')
	st.markdown('**3. Building Machine Learning Models  -** Machine learning model building is like teaching a computer to learn by showing it examples.')

	activities = ["EDA","Visualizations For Linear Models","Building Machine Learning Models"]	
	choice = st.sidebar.selectbox("Select Services",activities)

	if choice == 'EDA':
		st.title("Exploratory Data Analysis")

		data = st.file_uploader("Upload a dataset (only csv type supported)", type=["csv"])
		if data is not None:
			df = load.read_csv(data)
			st.dataframe(df.head())
			st.success("Data frame loaded successfully")
			

			if st.checkbox("Datatypes"):
				st.write(dataframe.show_dtypes(df))

			if st.checkbox("Dataset Columns"):
				st.write(dataframe.show_columns(df))

			if st.checkbox("Missing Values"):
				st.write(dataframe.Show_Missing1(df))

			if st.checkbox("Describe Column"):
				st.write(info.Column_information(df))

			if st.checkbox("Aggregation Tabulation"):
				st.write(dataframe.Tabulation(df))

			if st.checkbox("Num Count Summary"):
				st.write(info.num_count_summary(df))

			if st.checkbox("Statistical Summary"):
				st.write(info.statistical_summary(df))		
                
			if st.checkbox("Select Columns"):
				selected_columns = st.multiselect("Select Columns",dataframe.show_columns(df))
				new_df = df[selected_columns]
				st.dataframe(new_df)

			if st.checkbox("Numerical Variables"):
				num_df = dataframe.Numerical_variables(df)
				numer_df=pd.DataFrame(num_df)                
				st.dataframe(numer_df)

			if st.checkbox("Categorical Variables"):
				new_df = dataframe.categorical_variables(df)
				catego_df=pd.DataFrame(new_df)                
				st.dataframe(catego_df)

			if st.checkbox("DropNA"):
				imp_df = dataframe.impute(num_df)
				st.dataframe(imp_df)


			if st.checkbox("Missing Values present after DropNA"):
				st.write(dataframe.Show_Missing(imp_df))
               

			all_columns_names = dataframe.show_columns(df)
			all_columns_names1 = dataframe.show_columns(df)            
			selected_columns_names = st.selectbox("Select Column 1 for Cross Tabulation",all_columns_names)
			selected_columns_names1 = st.selectbox("Select Column 2 for Cross Tabulation",all_columns_names1)
			if st.button("Generate Cross Tab"):
				st.dataframe(pd.crosstab(df[selected_columns_names],df[selected_columns_names1]))


			all_columns_names3 = dataframe.show_columns(df)
			all_columns_names4 = dataframe.show_columns(df)            
			selected_columns_name3 = st.selectbox("Select Column 1 for Pearson Correlation (Numerical Columns)",all_columns_names3)
			selected_columns_names4 = st.selectbox("Select Column 2 for Pearson Correlation (Numerical Columns)",all_columns_names4)
			if st.button("Generate Pearson Correlation"):
				df=pd.DataFrame(dataframe.Show_pearsonr(imp_df[selected_columns_name3],imp_df[selected_columns_names4]),index=['Pvalue', '0'])
				st.dataframe(df)  

			spearmanr3 = dataframe.show_columns(df)
			spearmanr4 = dataframe.show_columns(df)            
			spearmanr13 = st.selectbox("Select Column 1 for Spearman Correlation (Categorical Columns)",spearmanr4)
			spearmanr14 = st.selectbox("Select Column 2 for Spearman Correlation (Categorical Columns)",spearmanr4)
			if st.button("Generate Spearman Correlation"):
				df=pd.DataFrame(dataframe.Show_spearmanr(catego_df[spearmanr13],catego_df[spearmanr14]),index=['Pvalue', '0'])
				st.dataframe(df)

			st.subheader("UNIVARIATE ANALYSIS")
			
			all_columns_names = dataframe.show_columns(df)         
			selected_columns_names = st.selectbox("Select Column for Histogram ",all_columns_names)
			if st.checkbox("Show Histogram for Selected Variable"):
				st.write(dataframe.show_hist(df[selected_columns_names]))
				st.pyplot()		

			all_columns_names = dataframe.show_columns(df)         
			selected_columns_names = st.selectbox("Select Columns for Distplot ",all_columns_names)
			if st.checkbox("Show DisPlot for Selected Variable"):
				st.write(dataframe.Show_DisPlot(df[selected_columns_names]))
				st.pyplot()

			all_columns_names = dataframe.show_columns(df)         
			selected_columns_names = st.selectbox("Select Columns for CountPlot ",all_columns_names)
			if st.checkbox("Show CountPlot for Selected Variable"):
				st.write(dataframe.Show_CountPlot(df[selected_columns_names]))
				st.pyplot()

			st.subheader("BIVARIATE ANALYSIS")

			Scatter1 = dataframe.show_columns(df)
			Scatter2 = dataframe.show_columns(df)            
			Scatter11 = st.selectbox("Select Column 1 for Scatter Plot (Numerical Columns)",Scatter1)
			Scatter22 = st.selectbox("Select Column 2 for Scatter Plot (Numerical Columns)",Scatter2)
			if st.button("Generate Plotly Scatter Plot"):
				st.pyplot(dataframe.plotly(df,df[Scatter11],df[Scatter22]))
                
			bar1 = dataframe.show_columns(df)
			bar2 = dataframe.show_columns(df)            
			bar11 = st.selectbox("Select Column 1 for Bar Plot ",bar1)
			bar22 = st.selectbox("Select Column 2 for Bar Plot ",bar2)
			if st.button("Generate Plotly Histogram Plot"):
				st.pyplot(dataframe.plotly_histogram(df,df[bar11],df[bar22]))                

			violin1 = dataframe.show_columns(df)
			violin2 = dataframe.show_columns(df)            
			violin11 = st.selectbox("Select Column 1 for Violin Plot",violin1)
			violin22 = st.selectbox("Select Column 2 for Violin Plot",violin2)
			if st.button("Generate Plotly Violin Plot"):
				st.pyplot(dataframe.plotly_violin(df,df[violin11],df[violin22]))  

			st.subheader("MULTIVARIATE ANALYSIS")

			if st.checkbox("Show Histogram"):
				st.write(dataframe.show_hist(df))
				st.pyplot()

			if st.checkbox("Show HeatMap"):
				st.write(dataframe.Show_HeatMap(df))
				st.pyplot()

			if st.checkbox("Show PairPlot"):
				st.write(dataframe.Show_PairPlot(df))
				st.pyplot()

			if st.button("Generate Word Cloud"):
				st.write(dataframe.wordcloud(df))
				st.pyplot()

	elif choice == 'EDA For Linear Models':
		st.title("EDA For Linear Models")
		data = st.file_uploader("Upload a dataset (only csv type supported)", type=["csv"])
		if data is not None:
			df = load.read_csv(data)
			st.dataframe(df.head())
			st.success("Data frame loaded successfully")


			all_columns_names = dataframe.show_columns(df)         
			selected_columns_names = st.selectbox("Select Columns for qqplot ",all_columns_names)
			if st.checkbox("Show qqplot for Selected Variable"):
				st.write(dataframe.qqplot(df[selected_columns_names]))
				st.pyplot()

			all_columns_names = dataframe.show_columns(df)         
			selected_columns_names = st.selectbox("Select Columns for Outliers ",all_columns_names)
			if st.checkbox("Show Outliers for Selected Variable"):
				st.write(dataframe.outlier(df[selected_columns_names]))

			if st.checkbox("Show Distplot for Selected Columns"):
				selected_columns_names = st.selectbox("Select Columns for Distplot ",all_columns_names)
				st.dataframe(dataframe.show_displot(df[selected_columns_names]))
				st.pyplot()

			con1 = dataframe.show_columns(df)
			con2 = dataframe.show_columns(df)            
			conn1 = st.selectbox("Select 1st Columns for chi square test",con1)
			conn2 = st.selectbox("Select 2st Columns for chi square test",con2)
			if st.button("Generate chi square test"):
				st.write(dataframe.check_cat_relation(df[conn1],df[conn2],0.5))
			

	elif choice == 'Machine Learning Model Building':
		st.title("Machine Learning Model Building for Classification Problem")
		data = st.file_uploader("Upload a dataset (only csv type supported)", type=["csv"])
		if data is not None:
			df = load.read_csv(data)
			st.dataframe(df.head())
			st.success("Data frame loaded successfully")

			if st.checkbox("Select your Variables  (Target Variable should be at last)"):
				selected_columns_ = st.multiselect("Select Columns for separation ",dataframe.show_columns(df))
				sep_df = df[selected_columns_]
				st.dataframe(sep_df)

			if st.checkbox("Show Indpendent Data"):
				x = sep_df.iloc[:,:-1]
				st.dataframe(x)

			if st.checkbox("Show Dependent Data"):
				y = sep_df.iloc[:,-1]
				st.dataframe(y)

			if st.checkbox("Dummy Variable"):
				x = dataframe.dummy(x)
				st.dataframe(x)

			if st.checkbox("Imputer (imputation transformer) "):
				x = model.IMpupter(x)
				st.dataframe(x)

			if st.checkbox("Compute Principle Component Analysis"):
				x = dataframe.PCA(x)
				st.dataframe(x)

			if st.checkbox("DropNA"):
				num_df = dataframe.Numerical_variables(df)
				imp_df = dataframe.impute(num_df)
				st.dataframe(imp_df)


			st.subheader("TRAIN TEST SPLIT")


			if st.checkbox("Select X Train"):
				from sklearn.model_selection import train_test_split
				x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
				st.dataframe(x_train)

			if st.checkbox("Select x_test"):
				from sklearn.model_selection import train_test_split
				x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
				st.dataframe(x_test)

			if st.checkbox("Select y_train"):
				from sklearn.model_selection import train_test_split
				x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
				st.dataframe(y_train)

			if st.checkbox("Select y_test"):
				from sklearn.model_selection import train_test_split
				x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
				st.dataframe(y_test)

			st.subheader("MODEL BUILDING")
			st.write("Build your BaseLine Model")

			if st.checkbox("Logistic Regression "):
				x = model.Logistic_Regression(x_train,y_train,x_test,y_test)
				st.write(x)

			if st.checkbox("Decision Tree "):
				x = model.Decision_Tree(x_train,y_train,x_test,y_test)
				st.write(x)

			if st.checkbox("Random Forest "):
				x = model.RandomForest(x_train,y_train,x_test,y_test)
				st.write(x)

			if st.checkbox("Naive_Bayes "):
				x = model.naive_bayes(x_train,y_train,x_test,y_test)
				st.write(x)

			if st.checkbox("XGB Classifier "):
				x = model.XGb_classifier(x_train,y_train,x_test,y_test)
				st.write(x)


	st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)


if __name__ == '__main__':
	load = DataFrame_Loader()
	dataframe = EDA_Dataframe_Analysis()
	info = Attribute_Information()
	model = Data_Base_Modelling()
	main()
 