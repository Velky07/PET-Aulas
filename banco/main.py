from bancoLibb import Banco

print("Bem vindo")
bancoUfrpe= Banco("Belk Inc.")
Banco.executarMenu()
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
    Banco.executarMenu()
    escolha= int(input("Digite a opção desejada:"))