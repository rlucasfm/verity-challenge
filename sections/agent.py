import streamlit as st
from inference.agent_graph import AgentGraphInferencer

st.title('Agente LangGraph')

input_text = st.text_input("Digite algo")
button = st.button("Enviar")

if button:
    inferencer = AgentGraphInferencer()
    st.write(inferencer.infer(input_text))
