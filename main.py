"""
Integrantes: Fabrício Silvany, Victor Andrade, Jonatas Fernandes
"""
import os
os.system("cls || clear")
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Menu
def menu():
    print("==|BILIOTECA DIGITAL|==")
    print("""
    1 | Adicionar livro
    2 | Procurar livro
    3 | Listar Livros
    4 | Adcionar assinante
    5 | Listar assinantes
    """)

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

while True:
    menu()
    opcao =int(input("\n Digite sua opção: "))

    match(opcao):
        case 1:
            os.system("cls || clear")
            #1 | Adicionar livro
            titulo_livro = input("Insira o titulo do livro: ")
            valor_livro = float(input("Insira o preço do livro:"))

            livro = Livro(livro_nome = titulo_livro, preco_livro = valor_livro)

            session.add(livro)
            session.commit()
        
        case 2:
            os.system("cls || clear")
            #2 | Procurar livro
            pass
        case 3:
            os.system("cls || clear")
            #3 | Listar Livros
            pass
        case 4:
            os.system("cls || clear")
            #4 | Adicionar assinante
            registro_nome_assinante = input("Insira o titulo do livro: ")
            registro_email_assinante = float(input("Insira o preço do livro:"))

            assinante = Assinante(nome_assinante=registro_nome_assinante, email_assinante = registro_email_assinante)

            session.add(assinante)
            session.commit()

        case 5:
            os.system("cls || clear")
            #5 | Listar assinantes
            pass        
        case _:
            os.system("cls || clear")
            print("Opção invalida \nTente novamente \n")