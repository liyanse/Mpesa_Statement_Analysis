import streamlit as st

def main():
    st.title("Read file types into the system")
    st.markdown(' Select service from the service menus, we offer services such as;')
    
    dataset_types = ['.csv','.xlsx','.json','.txt']
    
    result = st.selectbox('Select file type', dataset_types)
    st.write(f'Reading file type:{result}')