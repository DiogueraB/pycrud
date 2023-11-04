import os

# Classe para interface do usuário do programa

class Interface:
    # Construtor
    def __init__(self):
        pass

    def logotipo(self):
        print("==================================================")
        print("=============== Catálogo de Filmes ===============")
        print("==================================================")

    def limpatela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuário escolher uma opção
    # opcoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Desafio 1 
        # Verifique se a opcaoSelecionada é um número
        # inteiro válido, senão peça para tentar novamente

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)
            
        # Tenta converter para números
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)
            
        # Verifica se a opção selecionada é uma das opções válidas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário 
        return opcaoSelecionada

    def mostraMenuPrincipal(self):
        print ()
        print ("1 - Cadastrar Filmes")
        print ("2 - Lista de Filmes")
        print ("0 - Sair")
        print ()

