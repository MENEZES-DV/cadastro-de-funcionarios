# dados / Cadastro_Funcionários

import json

funcionarios = {}
 
def salvar_dados():
    with open('funcionarios.json', 'w',) as colaboradores:
        json.dump (funcionarios, colaboradores, indent=4)

with open('funcionarios.json', 'r') as colaboradores: 
    funcionarios = json.load(colaboradores)