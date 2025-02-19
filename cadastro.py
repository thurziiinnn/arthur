# Programa de cadastro

cadastros = []

def adicionar_cadastro(nome, idade, peso, altura):
    cadastro = {
        'nome': nome,
        'idade': idade,
        'peso': peso,
        'altura': altura
    }
    print()
    cadastros.append(cadastro)
    print("Cadastro realizado com sucesso!")

def imprimir_cadastros():
    if not cadastros:
        print("Nenhum cadastro encontrado.")
    else:
        for i, cadastro in enumerate(cadastros):
            print(f"Cadastro {i+1}:")
            print(f"Nome: {cadastro['nome']}")
            print(f"Idade: {cadastro['idade']}")
            print(f"Peso: {cadastro['peso']}")
            print(f"Altura: {cadastro['altura']}")
            print()

def excluir_cadastro(indice):
    if 0 <= indice < len(cadastros):
        cadastros.pop(indice)
        print("Cadastro excluído com sucesso!")
    else:
        print("Índice de cadastro inválido.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar cadastro")
        print("2. Imprimir cadastros")
        print("3. Excluir cadastro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Informe seu nome: ")
            idade = int(input("Informe sua idade: "))
            peso = float(input("Informe seu peso: "))
            altura = float(input("Informe sua altura: "))
            adicionar_cadastro(nome, idade, peso, altura)
        elif opcao == "2":
            imprimir_cadastros()
        elif opcao == "3":
            indice = int(input("Informe o índice do cadastro a ser excluído (começando em 0): "))
            excluir_cadastro(indice)
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()