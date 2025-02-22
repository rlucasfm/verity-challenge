-- Database Client 8.1.6
 -- Host: 127.0.0.1 Port: 5432 Database: verity

CREATE TABLE Cliente (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  telefone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  saldo DECIMAL(10,2) NOT NULL DEFAULT 0
);
INSERT INTO Cliente(nome, endereco, telefone, email, saldo) VALUES
  ('João', 'Rua 1', '1234-5678', 'joao@exemplo.com', 100),
  ('Maria', 'Rua 2', '9876-5432', 'maria@exemplo.com', 200),
  ('Pedro', 'Rua 3', '5555-1234', 'pedro@exemplo.com', 150),
  ('Ana', 'Rua 4', '6789-0123', 'ana@exemplo.com', 1500),
  ('Luiza', 'Rua 5', '4321-9876', 'luiza@exemplo.com', 4000);

CREATE TABLE Produto (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  descricao VARCHAR(255) NOT NULL,
  preco DECIMAL(10,2) NOT NULL
);
INSERT INTO Produto(nome, descricao, preco) VALUES
  ('Sabonete', 'Sabonete de limpeza', 5),
  ('Shampoo', 'Shampoo de limpeza', 10),
  ('Creme dental', 'Creme dental de limpeza', 12),
  ('Lavador', 'Lavador de roupas', 15),
  ('Detergente', 'Detergente de roupas', 18),
  ('Papel higienico', 'Papel higienico', 3),
  ('Papel toalha', 'Papel toalha', 4),
  ('Creme de barbear', 'Creme de barbear', 6),
  ('Lampada', 'Lampada', 20),
  ('Notebook', 'Computador', 3000),
  ('Teclado', 'Teclado', 100),
  ('Mouse', 'Mouse', 50),
  ('Monitor', 'Monitor', 300),
  ('Fogao', 'Fogao', 500),
  ('Geladeira', 'Geladeira', 1000),
  ('Microondas', 'Microondas', 200),
  ('Ar condicionado', 'Ar condicionado', 800),
  ('TV', 'TV', 1200),
  ('Radio', 'Radio', 150),
  ('Telefone', 'Telefone', 50),
  ('Smartphone', 'Celular', 1500);

CREATE TABLE Transacao (
  id SERIAL PRIMARY KEY,
  id_cliente INTEGER NOT NULL REFERENCES Cliente(id),
  id_produto INTEGER NOT NULL REFERENCES Produto(id)
);
INSERT INTO Transacao(id_cliente, id_produto) VALUES
  (2, 2),
  (4, 3),
  (5, 10),
  (5, 11),
  (2, 9),
  (5, 18),
  (5, 4),
  (2, 20),
  (1, 15),
  (4, 10),
  (1, 10),
  (1, 17),
  (2, 3),
  (3, 15),
  (2, 16),
  (2, 8),
  (5, 17),
  (2, 20),
  (5, 21),
  (2, 7);
