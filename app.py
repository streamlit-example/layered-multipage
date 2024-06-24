import streamlit as st

st.set_page_config(layout="wide")

pages = {
    "top": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
    ],
    "🍎 Apple": [
        st.Page("pages/A.py", title="A", icon="🍎"),
        st.Page("pages/a-1.py", title="A-1", icon="🍎"),
    ],
    "🍌 Banana": [
        st.Page("pages/B.py", title="B", icon="🍌"),
        st.Page("pages/b-1.py", title="B-1", icon="🍌"),
        st.Page("pages/b-2.py", title="B-2", icon="🍌", url_path="banana-banana"),
    ],
}

pg = st.navigation(pages, position="hidden")


st.header("App1")

pg.run()
