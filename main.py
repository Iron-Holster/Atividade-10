"""
Integrantes: Fabrício Silvany, Victor Andrade, Jonatas Fernandes
"""
import os

from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Banco de dados
BANCO_DADOS = create_engine("sqlite:///banco_de_dados.db")

#Conexão com o banco de dados
Session = sessionmaker(bind=BANCO_DADOS)
session = Session()

#Tabela
Base = declarative_base

class Livro(Base):
    __tablename__ = "livros"

    #Campos da tabela
    id = Column("id", Integer, primary_key = True, autoincrement=True)
    livro_nome = Column("nome do livro", String)
    preco_livro = Column("preço do livro", Float)

    def __init__(self, livro_nome = str, preco_livro = float):
        self.livro_nome = livro_nome
        self.preco_livro = preco_livro

class Assinante(Base):
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_assinante = Column("nome assinante", String)
    email_assinante = Column("email", String)

#Criando tabela no banco de dados
Base.metadata.create_all(bind=BANCO_DADOS)

os.system("cls || clear")