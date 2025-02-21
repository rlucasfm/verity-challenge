import streamlit as st
from inference.simple_graph import SimpleGraphInferencer

st.title('Pipeline com GraphBuilder')

input_text = st.text_input("Digite algo")
button = st.button("Enviar")

if button:
    inferencer = SimpleGraphInferencer()
    st.write(inferencer.infer(input_text))
