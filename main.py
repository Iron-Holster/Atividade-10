"""
Integrantes: Fabrício Silvany || Victor Andrade || Jonatas Fernandes
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
    6 | Deletar Livro da biblioteca
    7 | Deletar assinante do sistema
    8 | Encerrar programa
    """)

#Banco de dados
BANCO_DADOS = create_engine("sqlite:///banco_de_dados.db")

#Conexão com o banco de dados
Session = sessionmaker(bind=BANCO_DADOS)
session = Session()

#Tabela
Base = declarative_base()

class Livros(Base):
    __tablename__ = "livros"

    #Campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    livro_nome = Column(String)
    preco_livro = Column(Float)

    def __init__(self, livro_nome="", preco_livro=0.0):
        self.livro_nome = livro_nome
        self.preco_livro = preco_livro


class Assinante(Base):
    __tablename__ = "assinantes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_assinante = Column("nome assinante", String)
    email_assinante = Column("email", String)

    def __init__(self, nome_assinante = str, email_assinante = str):
        self.nome_assinante = nome_assinante
        self.email_assinante = email_assinante

#Criando tabela no banco de dados
Base.metadata.create_all(bind=BANCO_DADOS)

os.system("cls || clear")

while True:
    menu()
    opcao =int(input("\n Digite sua opção: "))

    match(opcao):
        case 1:
            os.system("cls || clear")
            #1 | Adicionar livro
            titulo_livro = input("Insira o titulo do livro: ")
            valor_livro = float(input("Insira o preço do livro: "))

            livro = Livros(livro_nome=titulo_livro, preco_livro=valor_livro)

            session.add(livro)
            session.commit()
            os.system("cls || clear")

            print("Livro adicionado!\n")

        case 2:
            os.system("cls || clear")
            #2 | Procurar livro
            pass
        case 3:
            os.system("cls || clear")
            #3 | Listar Livros
            listar_livros = session.query(Livros).all
            pass
        case 4:
            os.system("cls || clear")
            #4 | Adicionar assinante
            registro_nome_assinante = input("Insira o nome do assinante: ")
            registro_email_assinante = input("Insira o email do assinante: ")

            assinante = Assinante(nome_assinante=registro_nome_assinante, email_assinante = registro_email_assinante)

            session.add(assinante)
            session.commit()
            os.system("cls || clear")
            
            print("Assinatura concluida\n")

        case 5:
            #5 | Listar assinantes       
            os.system("cls || clear")
            listar_assinantes = session.query(Assinante).all

            for assinante in listar_assinantes:
                print(f"Nome: {registro_nome_assinante} \nEmail: {registro_email_assinante}\n")
        case 6:
            #6 | Deletar Livro da biblioteca
            pass
        case 7:
            #7 | Deletar assinante do sistema
            pass
        case 8:
            #8 | Encerrar programa
            print("Fechando programa...")
            break
        case _:
            os.system("cls || clear")
            print("Opção invalida \nTente novamente \n")