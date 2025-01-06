import streamlit as st

st.set_page_config(
  page_title="Corteza How-to Guide",
  page_icon="📖",
  layout="wide")

st.markdown("# Corteza How-to Guide")
st.sidebar.markdown("""
  # Corteza How-to Guide
  Hello there, you are reading the Coreza How-to guide. 
  
  Say thank to Google's AI-powered tools for helping me to make this document:
  """)

st.write("""
You can start with this guide by following some ways below:

- You don't want to read? Let's listen to this [AI-powered podcast](https://illuminate.google.com/library?play=Xso7nd__gfXO2) which briefs about Corteza features

- You are eager to try Corteza because you know exactly what you want from Corteza, and the docs are too long to read. At this time, you know you need to find a Corteza expert who will give you pieces of advice at no cost need to pay.
  So let's try [the NotebookLM by Google AI](https://notebooklm.google/) for a free domain expert. Just start by adding the [Corteza docs.md](<Corteza docs.md>) to the NotebookLM source, and then the AI will become a Corteza expert who will answer all your questions and not forget to include citations to the docs.

- Want to see the example? Google NotebookLM powers the document below or goes straight to [the example codes](https://github.com/phatle96/corteza-how-to?tab=readme-ov-file#common-corteza-workflow-task)
""")