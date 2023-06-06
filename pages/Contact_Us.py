import streamlit as st

st.header("Let Me Know If I Can Help You. Contact Me...")

with st.form(key ="email_forms"):
    user_email = st.text_input("PLEASE ENTER YOUR EMAIL ADDRESS BELOW: ")
    message = st.text_area("WRITE YOUR MESSAGE BELOW:")
    button = st.form_submit_button()

    if button:

        print("Pressed!")

