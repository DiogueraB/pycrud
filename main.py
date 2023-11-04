# Classe principal do programa
from interface import Interface
from bd import BD

# Classe principal do programa 
interface = Interface()

opcao = ""
while opcao != 0:
    interface.logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.limpatela()

    banco = BD("catalogoFilmes.db")