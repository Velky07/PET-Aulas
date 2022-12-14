from bancoLib import Banco

print("Bem vindo")
bancoUfrpe= Banco("Belk Inc.")
print("Menu")
print("1 - Criar nova conta")
print("2 - Consultar Saldo da conta")
print("3 - Depositar na conta")
print("4 - Sacar da conta")
print("5 - Render Poupança")
print("6 - Render bônus")
print("0 - Sair")
escolha= int(input("Digite a opção desejada:"))
while escolha>0:
    if escolha==1:
        #Criar Conta
        print("Criando conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))
        if opcao == 1:
            n = bancoUfrpe.criarCorrente()
        elif opcao == 2:
            n = bancoUfrpe.criarPoupanca()
        else:
            n = bancoUfrpe.criarBonificada()
        print("Conta criada\nO número da conta é:",n)
    elif escolha==2:
        #Consultar Conta
        n= int(input("Digite o número da sua conta: "))
        Saldo=bancoUfrpe.consultaSaldo(n)
        print("O saldo da conta" , n , "é de: R$", Saldo)
    elif escolha==3:
        #Depositar na Conta
        n= int(input("Digite o número da sua conta: "))
        valor= float(input("Digite o valor a ser depositado: "))
        Dep=bancoUfrpe.depositarComDesconto(n, valor)
        Saldo=bancoUfrpe.consultaSaldo(n)
        print("Dinheiro Depositado!\nO saldo atual da conta" , n , "é de: R$", Saldo)
    elif escolha==4:
        #Sacar da Conta
        n= int(input("Digite o número da sua conta: "))
        valor= float(input("Digite o valor a ser sacado: "))
        Sac= bancoUfrpe.sacar(n, valor)
        Saldo= bancoUfrpe.consultaSaldo(n)
        if Sac:
            print("Dinheiro Sacado!")
        else:
            print("Saldo insuficiente...\n\n\n")
        print("O saldo atual da conta" , n , "é de: R$",Saldo)
    elif escolha == 5:
        n= int(input("Digite o numero da conta poupanca:"))
        tratar= int(input("Digite quantos por cento sua poupança irá render:"))
        rend= bancoUfrpe.renderPoupanca(n, tratar)
        Saldo= bancoUfrpe.consultaSaldo(n)
        if rend:
            print("Poupanca com novo saldo")
        else:
            print("A conta não é poupanca ou não existe")
        print("O saldo atual da conta" , n , "é de: R$", Saldo)
    elif escolha == 6:
        print("Rendendo Bônus...")
        n = int(input("digite o numero da conta bonificada:"))
        resp = bancoUfrpe.renderBonus(n)
        Saldo= bancoUfrpe.consultaSaldo(n)
        if resp:
            print("Bonificada com novo saldo")
        else:
            print("A conta não é bonificada ou não existe")
        print("O saldo atual da conta" , n , "é de: R$", Saldo)
    escolha= int(input("Digite a opção desejada:"))