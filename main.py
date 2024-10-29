"""
Integrantes: Fabrício Silvany, Victor Andrade, Jonatas Fernandes
"""
import os

from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Banco de dados
BANCO_DADOS_LIVROS = create_engine("sqlite:///dados_dos_livros.db")

#Conexão com o banco de dados
Session = sessionmaker(bind=BANCO_DADOS_LIVROS)
session = Session()

#Tabela
Base = declarative_base()

class Livro(Base):
    __tablename__ = "livros"

    #Campos da tabela
    id = Column("id", Integer, primary_key = True, autoincrement=True)
    livro_nome = Column("nome do livro", String)
    preco_livro = Column("preço do livro", Float)

    def __init__(self, livro_nome = str, preco_livro = float):
        self.livro_nome = livro_nome
        self.preco_livro = preco_livro

#Segundo banco de dados
BANCO_DADOS_ASSINANTES = create_engine("sqlite:///dados_dos_assinantes.db")

#Cinexão com o segundo banco de dados
Session = sessionmaker(bind=BANCO_DADOS_ASSINANTES)
session = Session()

#Segunda tabela
Base = declarative_base()

class Assinante(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_assinante = Column("nome assinante", String)
    email_assinante = Column("email", String)

    def __init__(self, nome_assinante = str, email_assinante = str):
        self.nome_assinante = nome_assinante
        self.email_assinante = email_assinante

#Criando tabela no banco de dados
Base.metadata.create_all(bind=BANCO_DADOS_LIVROS)
Base.metadata.create_all(bind=BANCO_DADOS_ASSINANTES)

os.system("cls || clear")