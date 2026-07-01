import streamlit as st

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