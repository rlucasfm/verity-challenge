import streamlit as st

st.title('Home - Desafio Verity')

st.header("Introdução")

st.write("Esta é uma pequena coleção de agentes de IA que podem processar linguagem natural e criar queries SQL para acessar dados de um banco de dados PostgreSQL.")

st.header("Como usar o sistema")

st.write("Para usar o sistema, use a barra lateral para selecionar qual agente será usado. Em seguida, basta digitar uma pergunta ou comando no campo de texto abaixo.")

st.write("O sistema irá processar a linguagem natural e criar uma query SQL para acessar os dados do banco de dados.")

st.write("Os resultados serão exibidos abaixo.")

st.header("Exemplos de uso")

st.write("Aqui estão alguns exemplos de como usar o sistema:")

st.write("* Quais são os clientes que compraram o produto X?")
st.write("* Qual é o saldo do cliente Y?")
st.write("* Quais são os produtos que o cliente Z comprou?")