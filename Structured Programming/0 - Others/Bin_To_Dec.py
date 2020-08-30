# Conversion of a binary number to decimal number.
# Conversão de um número binário para número decimal.

# Recebe um número Binário qualquer
bin_num = input("Digite um número binário: ")

i = 0 # Define o índice inicial
res = 0 # Define um valor incial para variável res

# Equanto o número da posição do caractére for menor que o comprimento do número binário
while i < len(bin_num):
    # Pega o valor do caractére na posição i do número binário começando pela posição 0
    # Exemplo: 101 (o 3º caractére do número binário é igual á '1')
    num = int(bin_num[i])
    
    res += num * (2**i)
    i += 1
else:
    print("Resultado final:", res)

