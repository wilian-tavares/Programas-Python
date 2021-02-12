import random
import os

cont = 0

ddz = []
mega_sena = []
lotofacil = []

print("Seja bem vindo ao Mundo das Loterias !!!!!")
print()
print("Informe a sua opção Desejada.")
print()

opcao = input("Digite 1 Para Jogo do bicho: \nDigite 2 Para Loterias: ")
print()

if opcao == "1":
    print("****** Informe seu jogo ******")
    jogo = input("Digite 1 para Centena: \nDigite 2 para Milhar: \nDigite 3 para DDZ: ")
    print("--------------")
    print()
    if jogo == "1":
        centena = random.randint(000,100)
        print("A Centena Sorteada foi: ",centena)

    elif jogo == "2":
        milhar = random.randint(0000,9999)
        print("A Milhar Sorteada foi: ",milhar)

    elif jogo == "3":
        while cont != 2:
            sorteado = random.randint(00,99)
            if sorteado not in ddz:
                ddz.append(sorteado)
                cont += 1
        print("DDZ: ",ddz)

        '''Fim do bloco Jogo Do bicho'''
elif opcao == "2":
    print("Informe seu jogo")


    jogo = input("Digite 1 para Mega-Sena\nDigite 2 Lotofácil")
    if jogo == "1":

        while cont != 6:
            sorteado = random.randint(1,60)
            if sorteado not in mega_sena:
                mega_sena.append(sorteado)
                cont += 1
            elif sorteado in mega_sena:
                sorteado = random.randint(1,60)

        mega_sena.sort()
        print("MEGA-SENA",mega_sena)

    elif jogo == "2":
        while cont != 15:
            sorteado = random.randint(1,25)
            if sorteado not in lotofacil:
                lotofacil.append(sorteado)
                cont += 1
            elif sorteado in lotofacil:
                sorteado = random.randint(1,25)

        lotofacil.sort()
        print("LOTOFÁCIL",lotofacil)



os.system("pause")