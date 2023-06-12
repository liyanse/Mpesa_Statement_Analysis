from utils import *
from files import *
from clean import *
from sort import *

def main():

    st.title("Automated Data Analysis")    
    activities = ["Exploratory data analysis","Grouping","Visualization"]	
    
    choice = st.sidebar.selectbox("Select Services",activities)
    
    
    if choice == 'Exploratory data analysis':
        st.title("Exploratory Data Analysis")
        
        st.markdown(" The supported dataset types are json, csv, text and excel sheets")
                
        data = st.file_uploader("Upload a dataset", type=['csv', 'json', 'txt', 'xlsx'])
        
        if data is not None:
            # Get the file extension
            extension = data.name.split('.')[-1]
            # Load the data using the appropriate method
            if extension == 'csv':
                df = load.read_csv(data)
            elif extension == 'json':
                df = load.read_json(data)
            elif extension == 'txt':
                df = load.read_txt(data)
            elif extension == 'xlsx':
                df = load.read_excel(data)

            st.dataframe(df.head())
            st.success("Data frame loaded successfully")
            
            st.title("Understanding your DataFrame")
            
            if st.checkbox("Shape"):
                st.write(dataframe.show_shape(df))
                    
            if st.checkbox("Columns"):
                st.write(dataframe.show_columns(df))
            
            if st.checkbox("DataTypes"):
                st.write(dataframe.show_dtypes(df))
                                                
            if st.checkbox("Describe"):
                st.write(info.num_count_summary(df))
            
            if st.checkbox("Statistical Summary"):
                st.write(info.statistical_summary(df))		
            
            if st.checkbox("Select Columns"):
                selected_columns = st.multiselect("Select Columns",dataframe.show_columns(df))
                new_df = df[selected_columns]
                st.dataframe(new_df)
                        
                
            st.title("Cleaning your DataFrame")
            
            if st.checkbox("Show Duplicated"):
                st.write(clean.get_duplicate_values(df))
            
            if st.checkbox("Drop Duplicates"):
                st.write(clean.fill_duplicate_values(df))	
            
            if st.checkbox("Show Null Values"):
                st.write(clean.get_missing_values(df))
            
            if st.checkbox("Drop Null Values"):
                st.write(clean.drop_missing_values(df))
            
            if st.checkbox("Fill Null Values"):
                st.write(clean.fill_missing_values(df))
            # Check if user wants to select columns
            if st.checkbox("Group Columns"):
                # Get selected columns
                selected_columns = st.multiselect("Group Columns", df.columns)
                grouped_df = df.groupby(by=selected_columns)
                 # Display the grouped DataFrame
                st.dataframe(grouped_df)
    
    elif choice == 'Grouping':
        st.title("Group Data")
          
        
    elif choice == 'Visualization':
        st.title("Visualize and Generate Reports")

if __name__ == '__main__':
    load = Load_Dataset()
    dataframe = Understand_Datafame()
    info = Attribute_Information()
    clean = Clean_Dataframe()
    group = Group_By()
    main()
 
 