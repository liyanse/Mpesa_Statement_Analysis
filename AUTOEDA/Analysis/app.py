from utils import *
from files import *

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

  

if __name__ == '__main__':
    load = Load_Dataset()
    main()
 
 