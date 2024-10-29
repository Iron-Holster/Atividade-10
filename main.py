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


#Funções
def adicionar_livro(livro):
        os.system("cls || clear")
        #1 | Adicionar livro
        titulo_livro = input("Insira o titulo do livro: ")
        valor_livro = float(input("Insira o preço do livro: "))

        livro = Livros(livro_nome=titulo_livro, preco_livro=valor_livro)

        session.add(livro)
        session.commit()

def procurar_livro(livro):
        os.system("cls || clear")

        busca_titulo = input("Informe o nome do livro para busca: ")
        os.system("cls || clear")
        nome_livro = session.query(Livros).filter_by(titulo_livro = busca_titulo).first()

        print(f"Dados do livro: \nId: {livro.id} \nTítulo: {livro.livro_nome} \nPreço: {livro.preco_livro}")

        return nome_livro

def listar_livros(livro):
    os.system("cls || clear")
    lista_livros = session.query(Livros).all()
    
    for livros in lista_livros:
        print(f"Título do livro: {livros.livro_nome} \nPreço do livro: {livros.preco_livro}\n")

def adicionar_assinante(assinante):
    os.system("cls || clear")
    registro_nome_assinante = input("Insira o nome do assinante: ")
    registro_email_assinante = input("Insira o email do assinante: ")

    assinante = Assinante(nome_assinante=registro_nome_assinante, email_assinante = registro_email_assinante)

    session.add(assinante)
    session.commit()

def listar_assinantes(assinante):
        os.system("cls || clear")
        lista_assinantes = session.query(Assinante).all

        for assinantes in lista_assinantes:
            print(f"Nome: {assinantes.nome_assinante} \nEmail: {assinantes.email_assinante}\n")


os.system("cls || clear")

while True:
    menu()
    opcao =int(input("\n Digite sua opção: "))

    match(opcao):
        case 1:
            #Adicionando livros
            adicionando_livro = adicionar_livro(opcao)
            adicionando_livro
            os.system("cls || clear")
            print("Livro adicionado!\n")

        case 2:
            #Procurando livros
            busca_livros = procurar_livro(opcao)
            busca_livros

        case 3:
            #3 | Listar Livros
            listando_livros = listar_livros(opcao)
            listando_livros

        case 4:
            #4 | Adicionar assinante
            adicionando_assinante = adicionar_assinante(opcao)
            adicionando_assinante
            os.system("cls || clear")
            print("Assinatura concluida\n")

        case 5:
            #5 | Listar assinantes       
            os.system("cls || clear")
            listar_assinantes = session.query(Assinante).all

            for assinante in listar_assinantes:
                print(f"Nome: {registro_nome_assinante} \nEmail: {registro_email_assinante}\n")

        case _:
            os.system("cls || clear")
            print("Opção invalida \nTente novamente \n")