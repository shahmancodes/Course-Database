import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Course Finder", page_icon="🤖")


universities= ["HKU", "HKUST", "CUHK"]


st.title("Find your course match!")
st.markdown(
    "This mini-app finds a course very similar to yours from another university. Help us grow!"
)

university = st.selectbox(
    label="Your university",
    options=universities,
)

course = st.text_input(
    label="Your course code",
    placeholder="COMP 2011",
)

def findcourse():
    with st.spinner('Wait for it...'):
        my_bar = st.progress(0, text="")
        time.sleep(5)
        my_bar = st.progress(100, text="")

    st.success('Done!')
    #prediction= findcourse(##variables

st.button("Find a course!", on_click=findcourse(),type="primary", use_container_width=True )

def findcourse():
    with st.spinner('Wait for it...'):
        my_bar = st.progress(0, text="")
        time.sleep(5)
        my_bar = st.progress(100, text="")

    st.success('Done!')
    #prediction= findcourse(##variables)

prediction= [["HKUST","COMP 2012"],["HKUST", "COMP 2611"],["HKUST","COMP 2711"] ]

df = pd.DataFrame(
    [
    {"University":prediction[0][0],"Course": prediction[0][1], "Relevant": False},
    {"University":prediction[1][0],"Course": prediction[1][1], "Relevant": False},
    {"University":prediction[2][0],"Course": prediction[2][1], "Relevant": False},
   ]
)
edited_df = st.data_editor(df,hide_index=True)

st.markdown("Thank you, we will take your feedback into consideration 🎈")