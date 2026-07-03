import streamlit as st


name=st.text_input("enter your name")

st.title("take the input")

if st.buuton("submit"):
  st.write(f"print the name: {name}")
