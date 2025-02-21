import streamlit as st
import os

home = st.Page("sections/home.py", title="Home", icon=":material/home:")
agent = st.Page("sections/agent.py", title="Agente LangGraph", icon=":material/counter_1:")
simple = st.Page("sections/simple.py", title="Pipeline com GraphBuilder", icon=":material/counter_2:")

pg = st.navigation([home, agent, simple])
st.set_page_config(page_title="Desafio - Verity", page_icon=":material/edit:")
pg.run()