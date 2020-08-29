nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total de vendas:"))

comissao = salario * (15/100)
salario_final = salario + comissao

print(nome, " o seu salário fixo é de R$", salario, "e seu salário com a comissão é de R$" , salario_final)