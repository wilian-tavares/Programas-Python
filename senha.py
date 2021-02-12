import random

senha = input("Informe sua Senha:")

tamanho = len(senha)


nova = []

while senha != nova:

    for i in range(tamanho):
        gerador = random.randint(0, 9)
        nova.append(gerador)

print("Tamanho da Senha ",tamanho)
print(nova)