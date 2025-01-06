import streamlit as st

# Configure the page settings
st.set_page_config(page_title="Corteza How-to Guide", layout="wide")

pages= {
    "Home page": [
        st.Page("home.py", title="Corteza How-to Guide"),
    ],
    "Chat bot" : [
        st.Page("module-creator.py", title="Module Creator"),
        st.Page("./modules/corteza-chatbot.py", title="Corteza Chatbot"),
    ],
    "Resources": [
        st.Page("./modules/faqs.py", title="FAQs")
    ]
}

pg = st.navigation(pages)
pg.run()

