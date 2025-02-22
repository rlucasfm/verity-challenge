# Desafio Verity: Agente de IA com Langchain e LangGraph

Este é o meu código para o desafio proposto pela Verity, que consiste em criar um agente de IA usando Langchain e LangGraph que seja capaz de processar linguagem natural e criar queries SQL para acessar dados de um banco de dados PostgreSQL.

## Introdução

O desafio consiste em criar um agente de IA que possa processar o input do usuário e criar queries SQL para acessar dados de um banco de dados PostgreSQL. O banco de dados contém três tabelas: clientes, produtos e transações.
As queries devem ser válidas e seguras, e a partir dos exemplos mostrados, devem operar exclusivamente com operações de leitura, portanto impossibilitanto a alteração dos dados a partir dos inputs do usuário.

## Arquitetura do Sistema

O sistema é composto por três partes principais:

* **Langchain**: é uma biblioteca de IA que permite criar agentes de IA que possam processar linguagem natural.
* **LangGraph**: é uma biblioteca que permite criar grafos de conhecimento que possam ser usados para criar queries SQL.
* **PostgreSQL**: é o banco de dados que contém as tabelas de clientes, produtos e transações.

## Código

O código é dividido em três partes principais:

* **inference**: contém o código que define o agente de IA e como ele processa a linguagem natural.
* **sections**: contém o código que define as tabelas do banco de dados e como elas são acessadas.
* **main.py**: é o arquivo principal que define a interface do agente de IA e como ele é executado.
* **app.py**: é o arquivo que define a interface gráfica do agente de IA.

### inference

O código em `inference` define o agente de IA e como ele processa a linguagem natural. Ele utiliza a biblioteca Langchain para criar um agente de IA que possa processar linguagem natural.
Apesar de requerido apenas uma solução, neste projeto ofereci duas possibilidades de solução:
- Criando uma chain com o builder de Graphs do LangGraph, tento mais liberdade de operar manualmente em uma pipeline personalizada para a inferência.
- Utilizando um agente do LangGraph para uma resolução mais simples e que não é necessariamente uma opção linear, mas uma altenativa utilizando um agente ReAct (Com capacidade de Refletir - Agir).

### sections

O código em `sections` define as visões do Streamlit para a Interface de Usuário. Ele utiliza a biblioteca Streamlit para criar uma interface gráfica que possa ser usada para interagir com o agente de IA.

### app.py

O arquivo `app.py` define o entrypoint para o Streamlit e a interface gráfica do agente de IA.

### database.db
Banco de dados em SQLite para facilitar a exemplificação da solução proposta.
O banco está estruturado da seguinte forma:

* **Cliente**: contém as informações dos clientes: id, nome, endereço, telefone, email e saldo.
* **Produto**: contém as informações dos produtos: id, nome, descricao, preco.
* **Transacao**: contém as informações das transações: id, id_cliente, id_produto.

As tabelas tem o seguinte DDL:
CREATE TABLE Cliente (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(255) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  telefone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  saldo DECIMAL(10,2) NOT NULL
)

CREATE TABLE Produto (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(255) NOT NULL,
  descricao VARCHAR(255) NOT NULL,
  preco DECIMAL(10,2) NOT NULL
)

CREATE TABLE Transacao (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER NOT NULL,
  id_produto INTEGER NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
  FOREIGN KEY (id_produto) REFERENCES Produto(id)
)

## Conclusão

Este é o meu código para o desafio proposto pela Verity. Ele demonstra como utilizar as bibliotecas Langchain e LangGraph para criar um agente de IA que possa processar linguagem natural e criar queries SQL para acessar dados de um banco de dados PostgreSQL (Dentro do exemplo também mostrando com um banco SQLite, para facilitar o teste e a visualização no serviço gerenciado de hospedagem da Streamlit).