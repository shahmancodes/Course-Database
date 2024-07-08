import streamlit as st


pg = st.navigation([
    st.Page("PoC.py", title="CourseFinder", icon="🔥"),
    st.Page("Changelog.py", title="ChangeLog"),
    st.Page("Issues.py", title="Issues")
])
pg.run()