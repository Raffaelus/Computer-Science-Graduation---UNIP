nome = input("Digite o nome do aluno: ")
notas = list(range(3))

notas[0] = float(input("Digite a nota 1: "))
notas[1] = float(input("Digite a nota 2: "))
notas[2] = float(input("Digite a nota 3: "))

soma_notas = 0

for nota in notas:
    soma_notas += nota
else:
    media = soma_notas / len(notas)
    print(nome, "sua média foi de:", media)