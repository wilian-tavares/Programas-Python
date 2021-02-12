

arquivo = open("Arquivo.txt", "a")


conteudo = list()
frases = list()

sites = list()
emails = list()
senhas = list()


conteudo.append("***** Armazanamento de Senhas ***** \n")

print()
print("***** Armazanamento de Senhas ***** ".upper())
print()

opcao1 = "S"

while True:
    print("DESEJA CADASTRAR UMA NOVA SENHA? ")
    opcao1 = input("S ou N ? ").upper()
    if(opcao1 != "S"):
        print("Processo Finalizado")
        break

    print("Informe o Site, Email e Senha: ")
    site = input("Informe o Site: ")
    email = input("Informe seu Email: ")
    senha = input("Informe sua Senha: ")

    print()
    print("-"*50)
    print("CONFIRA OS DADOS")
    print("-" * 50)
    print("Site: ", site, "\nEmail: ", email, "\nSenha: ", senha)
    print()

    opcao2 = 0

    opcao2 = input("Os Dados Estão corretos?\n"
                   "S ou N ? ").upper()
    if opcao2 == "S":
        sites.append("SITE: " + site + " = ")
        emails.append("Email: " + email + " = ")
        senhas.append("SENHA: " + senha)
    elif opcao2 != "S":
        print("Dados Não Cadastrados")

    print()
    print("Email: ",email ,"\nSenha: ",senha, "\nOs dados Estão Corretos?")
    print()
    '''emails.append("Email: " + email + " = ")
    senhas.append("SENHA: " + senha)'''









#conteudo.append("***** Armazanamento de Senhas *****")#

emails.append("Email: "+ email + " = ")
senhas.append("SENHA: "+ senha)




#arquivo.writelines(conteudo)#
for i in range(len(emails) - 1):
    arquivo.writelines(sites[i])
    arquivo.writelines(emails[i])
    arquivo.writelines(senhas[i] + "\n")



arquivo.close()
