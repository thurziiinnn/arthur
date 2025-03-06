# Gerenciador de Contas

def criar_conta(contas, nome, senha):
    if nome in contas:
        print(f"Conta com o nome '{nome}' já existe.")
    else:
        contas[nome] = senha
        print(f"Conta '{nome}' criada com sucesso!")


def excluir_conta(contas, nome):
    if nome in contas:
        del contas[nome]
        print(f"Conta '{nome}' excluída com sucesso!")
    else:
        print(f"Conta com o nome '{nome}' não encontrada.")


def verificar_contas(contas):
    if contas:
        print("Contas existentes:")
        for nome in contas:
            print(f"Nome: {nome}")
    else:
        print("Nenhuma conta criada.")


def main():
    contas = {}
    while True:
        print("\nMenu de opções:")
        print("1. Criar conta")
        print("2. Excluir conta")
        print("3. Verificar contas")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            nome = input("Digite o nome da conta: ")
            senha = input("Digite a senha da conta: ")
            criar_conta(contas, nome, senha)
        elif opcao == '2':
            nome = input("Digite o nome da conta a ser excluída: ")
            excluir_conta(contas, nome)
        elif opcao == '3':
            verificar_contas(contas)
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
