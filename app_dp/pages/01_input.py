import streamlit as st

st.title("Streamlit Button Showcase")

st.header("1️. 通常ボタン")
if st.button('Click Me'):
    st.success("🎉 You clicked the button!")

st.header("2️. ディセーブル状態のボタン")
st.button('Disabled Button', disabled=True)