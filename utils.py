import streamlit as st
import time
def findcourse():
    with st.spinner('Wait for it...'):
        my_bar = st.progress(0, text="")
        time.sleep(2)
        my_bar. progress(100, text="")

    st.success('Done!')
