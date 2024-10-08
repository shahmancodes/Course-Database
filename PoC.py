import streamlit as st
import time
import pandas as pd
import dataloader
import utils
predictionbool=False
    

submittedcourse=False

st.set_page_config(page_title="Course Finder", page_icon="🤖")
st.title("Find your course match!")
st.markdown(
    "This mini-app finds a course very similar to yours from another university. Help us grow!")


universities= ["HKU", "HKUST", "CUHK"]


def take_input():
    global submittedcourse
    with st.form("uni_input"):
        university = st.selectbox(
        label="Your university",
        options=universities,
        )
        submitteduni =st.form_submit_button("Choose a Course!",type="primary", use_container_width=True )


    myuni, myunicourses, otheruni=dataloader.read_data(university)

    if submitteduni==True:
        with st.form("course_input"):
            course = st.selectbox(
                label="Your course code",
                placeholder="COMP 2011",
                options=myunicourses,
            )
            submittedcourse =st.form_submit_button("Find a matching course!",type="primary", use_container_width=True)
            



done= take_input()

prediction= [["HKUST","COMP 2012"],["HKUST", "COMP 2611"],["HKUST","COMP 2711"] ]
df = pd.DataFrame(
            [
            {"University":prediction[0][0],"Course": prediction[0][1], "Relevant": False},
            {"University":prediction[1][0],"Course": prediction[1][1], "Relevant": False},
            {"University":prediction[2][0],"Course": prediction[2][1], "Relevant": False},
            ]
    )
with st.form("confirm_courses"):

    edited_df = st.data_editor(df,hide_index=True, use_container_width=True, disabled=["University","Course"], on_change=None)
    edited =st.form_submit_button("Confirm!",type="primary", use_container_width=True )
    st.write("Thank you, your feedback will be very helpful in allowing us to improve! 🎈")
