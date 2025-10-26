# Prática dicionário
import time

iniciar = 0

def main():

    funcionarios = {}
    
    def cadastrar_funcionario():
        time.sleep(1)
        print("\n ____COM ATENÇÃO PREENCHA AS INFORMAÇÕES A SEGUIR PARA UM NOVO CADASTRO NO SISTEMA____ \n")

        nome_func = input("DIGITE O NOME COMPLETO DO COLABORADOR: ")
        time.sleep(0.5)
    
        while True:
            try:
                idade_func = int(input("DIGITE A IDADE DO COLABORADOR: "))
                
                if idade_func < 18: 
                        print("O funcionário deve ser maior de idade")
                else:
                    break

            except ValueError: 
                print("*ERRO* \n Digite um número válido para a idade.")

        time.sleep(0.5)
        cargo_func = input("DIGITE O CARGO QUE IRÁ EXERCER: ")

        novo_id = 1
        while novo_id in funcionarios:
            novo_id += 1
            
        funcionarios [novo_id] = {"nome": nome_func, "idade": idade_func , "cargo": cargo_func}

        time.sleep(1)
        print(f"\nNOVO FUNCIONÁRIO CADASTRADO: {funcionarios.get(novo_id)}\n")
        
    def listar_funcionários():
        print("______ LISTANDO FUNCIONÁRIOS ______\n")
        time.sleep(2)
        for chave, valor in funcionarios.items():  
            print(f" Funcionário {chave}: | {valor['nome']} ({valor['idade']} anos) - Cargo exercido: {valor['cargo']}") 
            time.sleep(0.5)

    def buscar_funcionario():
        listar_funcionários()
        try:
            Busca_func = int(input("QUAL O ID DO FUNCIONÁRIO QUE DESEJA BUSCAR?"))
            if Busca_func in funcionarios:
                print(funcionarios.get(Busca_func))
            else: 
                print("Este ID não exite, digite um o ID de um funcionário cadastrado no sistema")
        except ValueError: 
            print("Digite um ID Valido para buscar um funcionário")

    def remover_funcionario():
        listar_funcionários()
        try:
            remove_func = int(input("QUAL O ID DO FUNCIONÁRIO QUE DESEJA REMOVER"))
            if remove_func in funcionarios:
                funcionarios.pop(remove_func)
                print(f"FUNCIONÁRIO {remove_func} REMOVIDO")
            else: 
                print("Digite um ID Valido para buscar um funcionário")

        except ValueError: 
            print("Digite um ID Valido para remover um funcionário")

    while True:

        menu = {
            "1" : cadastrar_funcionario,
            "2" : listar_funcionários, 
            "3" : buscar_funcionario,
            "4" : remover_funcionario,
    
        }

        print (" 1- Cadastrar funcionário \n 2- Listar todos funcionários \n 3- Buscar funcionário \n 4- Remover funcionário \n 5- Encerrar sistema")

        operacao = input("QUAL O DIGITO DA OPERAÇÃO DESEJADA?: ")

        if operacao in menu: 
            menu[operacao]()

        elif operacao == "5":
            global iniciar
            iniciar = 0
            break
            
        else:
            print("\n ____ ESTÁ OPERAÇÃO NÃO EXISTE ____ \n")
            time.sleep(2)

while True:
        
    iniciar = int(input("Digite 1 para iniciar o programa"))

    while iniciar == 1:
        main()