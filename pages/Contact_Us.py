import streamlit as st
from send_email import send_email

st.header("Let Me Know If I Can Help You. Contact Me...")

with st.form(key ="email_forms"):
    user_email = st.text_input("PLEASE ENTER YOUR EMAIL ADDRESS BELOW: ")
    raw_message = st.text_area("WRITE YOUR MESSAGE BELOW:")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}"""
    button = st.form_submit_button()
    print(button)

    if button:
        send_email(message)
        st.info("Great! We gotch your email! Someone will get back to you shortly... ")

