# Função Main / Cadastro_funcionários

import time
import funcoes 
import dados

while True:

    print("___SISTEMA DE CADASTRO DE FUNCIONÁRIOS___\n")
    iniciar = int(input("DIGITE '1' PARA INICIAR O PROGRAMA: "))

    while iniciar == 1:

        while True:
            dados.salvar_dados() #Caso o dicionário ainda não exista, ele roda a função e já cria antes de realizar alguma ação dentro do programa. 
           
            menu = {
            
                "1" : funcoes.cadastrar_funcionario,
                "2" : funcoes.listar_funcionários, 
                "3" : funcoes.buscar_funcionario,
                "4" : funcoes.remover_funcionario,
            }

            print (" \n 1- Cadastrar funcionário \n 2- Listar todos funcionários \n 3- Buscar funcionário \n 4- Remover funcionário \n 5- Encerrar sistema \n")
            operacao = input("QUAL O DIGITO DA OPERAÇÃO DESEJADA?: ")

            if operacao in menu: 
                menu[operacao]()

            elif operacao == "5":
                print("\n***ENCERRANDO SISTEMA***\n")
                time.sleep(2)
                print("\n***SISTEMA ENCERRADO***\n")
                iniciar = 0
                break
                
            else:
                print("\n ____ ESTÁ OPERAÇÃO NÃO EXISTE ____ \n")
                time.sleep(2)