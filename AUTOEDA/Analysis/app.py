from utils import *
from files import *
from clean import *

def main():

    st.title("Exploratory Data Analysis")

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
              
        if st.checkbox("Null Values"):
            st.write(dataframe.get_missing_values(df))
          

if __name__ == '__main__':
    load = Load_Dataset()
    dataframe = Understand_Datafame()
    info = Attribute_Information()
    main()
 
 