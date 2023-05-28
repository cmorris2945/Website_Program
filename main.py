import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/lab_coat.jpg")

with col2:
    st.title("Chris Radston")
    content = """
        Hello! My name is Chris Radston. I am the Principal Bioinformatics Scientist for the State of Hawaii Center for 
        Disease Control and Prevention. With a Masters degree in Computer Science and a PhD in Biomedicine and Computer Science, I bring a unique blend of expertise to the dynamic field of bioinformatics.
        My role involves analyzing and interpreting complex biological data sets to help unravel the intricate mysteries of life. I apply advanced computational techniques and machine learning algorithms to 
        make sense of genomic sequences, protein structures, and metabolic pathways. My research primarily focuses on public health-related topics such as identifying genetic risk factors for diseases, 
        understanding the impact of environmental changes on pathogen evolution, and monitoring the spread of infectious diseases across the state.
       """
    st.info(content



