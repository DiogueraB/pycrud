import os
from bd import BD

# Classe para interface do usuário do programa

class Interface:
    # Construtor
    def __init__(self):
        self.banco = BD("catalogoFilmes.db")

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

    def mostraCadastroFilmes(self):
        self.logotipo()

        print("Insira os dados do Filme:")
        print("(campos com * são obrigatórios)")

        titulo = self.solicitaValor('Digite o título ', 'texto', False)
        genero = self.solicitaValor('Digite o gênero ', 'texto', False)
        duracao = self.solicitaValor('Digite a duração ', 'texto', True)
        diretor = self.solicitaValor('Digite o nome do diretor', 'texto', True)
        estudio = self.solicitaValor('Digite o nome do estúdio', 'texto', True)
        classificacao = self.solicitaValor('Digite a classificação', 'texto', True)
        ano = self.solicitaValor('Digite o ano', 'numero' , True)

        # Armazena os valores no banco de dados!
        valores = {
            "titulo": titulo,
            "genero": genero,
            "duracao": duracao,
            "diretor": diretor,
            
        }
        self.banco.inserir('filmes', )
    
    # Solicita um valor do usuário e valida ele
    # Return valordigitado
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo,permiteNulo)
        elif valor == "" and permiteNulo:
            return valor

        # Verifica se está no formato correto
        if tipo == 'numero':
            try: 
                valor = float(valor)
            except ValueError:
                print("Valor Inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            
        return valor