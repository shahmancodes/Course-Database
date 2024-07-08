import streamlit as st


pg = st.navigation([
    st.Page("PoC.py", title="CourseFinder", icon="🔥"),
    st.Page("Changelog.py", title="Updates", icon=":material/favorite:"),
])
pg.run()