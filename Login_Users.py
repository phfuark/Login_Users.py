import csv
import os

# Nome do arquivo onde os dados serão armazenados
FILE_NAME = "users.csv"

# Função para criar o arquivo CSV caso ele não exista
def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])

# Função para registrar um novo usuário
def register():
    print("\n--- Registro ---")
    username = input("Escolha um nome de usuário: ")
    password = input("Escolha uma senha: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("Usuário registrado com sucesso!\n")

# Função para realizar login
def login():
    print("\n--- Login ---")
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login bem-sucedido! Bem-vindo, {}!\n".format(username))
                return

    print("Usuário ou senha incorretos. Tente novamente.\n")

def main():
    initialize_csv()

    while True:
        print("--- Sistema de Login ---")
        print("1. Fazer Login")
        print("2. Registrar-se")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")




