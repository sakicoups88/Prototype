"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
df = pd.DataFrame({
'first column': [1, 2, 3, 4,5,6,10],
'second column': [10, 20, 30, 40,50,60,100],
'third column': [100, 200, 300, 400,500,600,1000],
'fourth column': [1000, 2000, 3000, 4000,5000,6000,10000]
})
df

import streamlit as st

st.title("Streamlit Button Showcase")

st.header("1️. 通常ボタン")
if st.button('Click Me'):
    st.success("🎉 You clicked the button!")

st.header("2️. ディセーブル状態のボタン")
st.button('Disabled Button', disabled=True)

st.header("3️. ボタンクリックでカウンター")
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Increment Counter"):
    st.session_state.count += 1
st.write("Counter value:", st.session_state.count)

st.header("4️. ボタンを押すとチェックボックスが現れる")
if st.button("Show Checkbox"):
    show_check = st.checkbox("New Checkbox appears!")
    if show_check:
        st.write("✅ Checkbox is checked!")

st.header("5️. ダブルクリック風ボタン")
if st.button("Step 1"):
    st.session_state.step1 = True

if st.session_state.get('step1'):
    if st.button("Step 2"):
        st.success("🎊 Step 2 completed after Step 1!")

st.header("6️. 同時に複数ボタン")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Button A"):
        st.write("🅰️ Button A clicked!")
with col2:
    if st.button("Button B"):
        st.write("🅱️ Button B clicked!")
with col3:
    if st.button("Button C"):
        st.write("🆑 Button C clicked!")

st.header("7️. アイコン付きボタン")
if st.button("🚀 Launch"):
    st.success("Rocket Launched!")

st.header("8️. 長押し判定")
# Streamlitに長押し検出はないため、擬似的にタイムスタンプを利用
import time
if st.button("Press me quickly"):
    st.write(f"⏱️ Clicked at: {time.time()}")

st.header("9️. ボタンクリック時にファイルを表示/ダウンロード")
sample_data = "Name,Score\nAlice,90\nBob,85"
if st.button("Show Sample CSV"):
    st.download_button("Download CSV", sample_data, file_name='sample.csv', mime='text/csv')
    st.text_area("CSV Content", sample_data, height=100)