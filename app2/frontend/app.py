import streamlit as st
import requests

st.title("Hello World!")

with st.form(key="form"):
    texte=st.text_input("écrire qqchose:")
    submit=st.form_submit_button("envoyer ")

if submit :
    response= requests.post("http://backend:5000/formulaire", json={"texte": texte})

