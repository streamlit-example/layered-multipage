import streamlit as st

__LAYER_RATIO = [1, 9]

__DISP_PETTERN = 2  # 1 or 2


def page_urls(is_A_expanded, is_B_expanded):
    with st.sidebar:
        st.page_link("pages/home.py", label="Home")

        st.markdown("---")

        st.markdown("### Fruits App")

        if __DISP_PETTERN == 1:
            with st.expander("Apple", icon="🍎", expanded=is_A_expanded):
                st.page_link("pages/a-1.py", label="a - 1")

            with st.expander("Banana", icon="🍌", expanded=is_B_expanded):
                st.page_link("pages/b-1.py", label="b - 1")
                st.page_link("pages/b-2.py", label="b - 2")
        else:
            st.page_link("pages/A.py", label="A", icon="🍎")
            if is_A_expanded:
                _, col = st.columns(__LAYER_RATIO)
                col.page_link("pages/a-1.py", label="a - 1")

            st.page_link("pages/B.py", label="B", icon="🍌")
            if is_B_expanded:
                _, col = st.columns(__LAYER_RATIO)
                col.page_link("pages/b-1.py", label="b - 1")
                col.page_link("pages/b-2.py", label="b - 2")

        st.markdown("---")

        st.markdown("### External Websites")
        st.page_link("http://www.google.com", label="Google", icon="🌎")
