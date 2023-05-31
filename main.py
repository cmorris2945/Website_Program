import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/lab_coat.jpg")


with col2:
    st.title("Chris Radston")
    content = """
        Hello! My name is Chris Radston. I am the Principal Bioinformatics Scientist for the State of Hawaii Center for 
        Disease Control and Prevention. With a Masters degree in Computer Science and a PhD in Biomedicine and Computer 
        Science, I bring a unique blend of expertise to the dynamic field of bioinformatics.
        My role involves analyzing and interpreting complex biological data sets to help unravel the intricate mysteries 
        of life. I apply advanced computational techniques and machine learning algorithms to 
        make sense of genomic sequences, protein structures, and metabolic pathways. My research primarily focuses on 
        public health-related topics such as identifying genetic risk factors for diseases, 
        understanding the impact of environmental changes on pathogen evolution, and monitoring the spread of
        infectious diseases across the state.
    
       """
    st.header("Summary of me...")
    st.info(content)

    content2 = """  Below, you can find some of the applications I have built and the qualifications and certifications I have,
        and if you would like to get in touch with me or hire me, I am available for temporary assignment,
        contract or permanent placement... """


st.info(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data (1).csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
