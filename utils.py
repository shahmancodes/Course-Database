import streamlit as st

def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name

def choose_course():
    with st.form("course_input", clear_on_submit=True):
        course = st.selectbox(
            label="Your course code",
            placeholder="COMP 2011",
            options=myunicourses,
        )
    # Every form must have a submit button.
        submitted =st.form_submit_button("Find a matching course!",type="primary", use_container_width=True )

if __name__ == "__main__":
    ...