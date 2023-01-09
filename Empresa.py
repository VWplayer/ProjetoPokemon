import json

class Funcionarios:
    def __init__(self,id,nome,salario):
        self._id = id
        self._nome = nome
        self._salario = salario

def adicionarFuncionario():
    novoNome = input("Digite o nome do funcionario novo:")
    novoSalario = float(input(f"Digite o salario de {novoNome}:"))
    novoFuncionario = Funcionarios(len(funcionários)+1,novoNome,novoSalario)
    funcionários.append(novoFuncionario)
    print(f"{novoFuncionario._nome} adicionado com sucesso!\n")


def salvarBanco(listaFuncionarios):
    novoBanco = []

    for f in listaFuncionarios:
        novoBanco.append({"ID": f._id, "Nome": f._nome, "Salario": f._salario})
    
    with open('banco.json', 'w') as nb:
        json.dump(novoBanco, nb, indent=2)

    print("Banco salvo")

with open('banco.json') as b:
 banco = json.load(b)
 print (banco)

funcionários = []

for funcionario in banco:
    funcionários.append(Funcionarios(funcionario["ID"],funcionario["Nome"],funcionario["Salario"]))
    

while(True):
    menu = input(f"""Escolha umas das opções:
    1. Ver funconários:
    2. Ver salário do Funcionário:
    3. Adcinoar funcionário:
    0. Sair da aplicação e salvar:""")

    match menu :
        case "1":
            for i in range(len(funcionários)):
                  print(f"{funcionários[i]._id} - {funcionários[i]._nome}")
            input("Insira qualquer tecla para continuar")
        case "2":
            for i in range(len(funcionários)):
                print(f"{funcionários[i]._id} - {funcionários[i]._nome}")
            op = int(input("Digite o id do funcionario que deseja ver o salario"))
            print(f"O salario do {funcionários[op-1]._nome} é R$ {funcionários[op-1]._salario}")
        case "3":
            adicionarFuncionario()
            input("Insira qualquer tecla para continuar")
        case "0":
            salvarBanco(funcionários)
            print("Aplicação finalizada e dados salvos")
            break
        case _:
            print("Opção inválida")