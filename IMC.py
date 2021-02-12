while True:

    nome = input("Informe seu Nome: ").upper()
    altura = float(input("Informe sua Altura: "))
    peso = float(input("Informe se Peso: "))
    imc = peso/(altura*altura)
    print()
    print("-" * 50)
    print(f"Olá,",nome, " Seu IMC é: , {:.2f}".format(imc))




    if imc < 18.5:
        print("Abaixo do Peso")
    elif imc >18.5 and imc < 24.9:
        print("Peso Normal")
    elif imc > 24.9 and imc < 29.9:
        print("Acima do Peso")
    elif imc > 29.9 and imc < 34.9:
        print("Obesidade Grau I")
    elif imc > 34.9 and 39.9:
        print("Obesidade Grau II")
    elif imc >= 40:
        print("Obesidade Mórbida")

    print("-"*50)
    print()
    print("Deseja Fazer outro Teste?")
    repetir = input("S / N: ").upper()
    if repetir != "S":
        break
print()
print("-"*50)
print("OBRIGADO POR USAR O APLICATIVO")
print("-"*50)
print()
cancelar = input("DIGITE QUALQUER TECLA PARA FECHAR O APP:")