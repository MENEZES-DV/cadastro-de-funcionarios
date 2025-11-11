# Funções / Cadastro_Funcionários

import time
import dados

def cadastrar_funcionario():
        
        time.sleep(1)
        print("\n ____COM ATENÇÃO PREENCHA AS INFORMAÇÕES A SEGUIR PARA UM NOVO CADASTRO NO SISTEMA____ \n")
        nome_func = input("DIGITE O NOME COMPLETO DO COLABORADOR: ")
        time.sleep(0.5)
    
        while True:
            try:
                idade_func = int(input("DIGITE A IDADE DO COLABORADOR: "))
                if idade_func < 18: 
                        print("\n***ERRO - O FUNCIONÁRIO DEVE SER MAIOR DE IDADE*** \n")
                else:
                    break
            except ValueError: 
                print("\n***ERRO - DIGITE UMA IDADE VÁLIDA*** \n")

        time.sleep(0.5)
        cargo_func = input("DIGITE O CARGO QUE IRÁ EXERCER: ")
        novo_id = 1

        while str(novo_id) in dados.funcionarios:
            novo_id += 1

        dados.funcionarios [str(novo_id)] = {"nome": nome_func, "idade": idade_func , "cargo": cargo_func}
        dados.salvar_dados()
        time.sleep(1)
        print(f"\nNOVO FUNCIONÁRIO CADASTRADO: {dados.funcionarios.get(str(novo_id))}")
        
def listar_funcionários():
        
        print("\n______ LISTANDO FUNCIONÁRIOS ______\n")
        time.sleep(2)

        for chave, valor in dados.funcionarios.items():
            print(f" Funcionário {chave}: | {valor['nome']} ({valor['idade']} anos) - Cargo exercido: {valor['cargo']}") 
            time.sleep(0.5)

             
def buscar_funcionario():
        
        listar_funcionários()
        Busca_func = input("\nDIGITE O ID DO FUNCIONÁRIO QUE DESEJA BUSCAR: ")

        if Busca_func in dados.funcionarios:
            print(dados.funcionarios.get(Busca_func))
        else: 
            print("\n***ID INVÁLIDO, DIGITE O ID DE UM FUNCIONÁRIO CADASTRADO***")
            buscar_funcionario()

def remover_funcionario():
        
        listar_funcionários()
        remove_func = input("DIGITE O ID DO FUNCIONÁRIO QUE DESEJA REMOVER: ")

        if remove_func in dados.funcionarios:
            dados.funcionarios.pop(remove_func)
            dados.salvar_dados()
            print(f"\nFUNCIONÁRIO {remove_func} REMOVIDO")
        else: 
            print("\n***ID INVÁLIDO, DIGITE UM ID CADASTRADO NO SISTEMA***")
            remover_funcionario()