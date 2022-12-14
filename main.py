import bancoLib

print("Bem vindo")
bancoVelky= bancoLib.Banco("Belk Inc.")
print("Menu")
print("1 - Criar nova conta")
print("2 - Consultar Saldo da conta")
print("3 - Depositar na conta")
print("4 - Sacar da conta")
print("5 - Deletar Conta")
print("0 - Sair")
escolha= int(input("Digite a opção desejada:"))
while escolha>0:
    if escolha==1:
        #Criar Conta
        print("Criando conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        opcao = int(input("digite o tipo da conta:"))
        if opcao == 1:
            n = bancoVelky.criarCorrente()
        else:
            n = bancoVelky.criarPoupanca()
        print("Conta criada\nO número da conta é:",n)
    elif escolha==2:
        #Consultar Conta
        n= int(input("Digite o número da sua conta: "))
        Saldo=bancoVelky.consultaSaldo(n)
        print("O saldo da conta" , n , "é de: R$", Saldo)
    elif escolha==3:
        #Depositar na Conta
        n= int(input("Digite o número da sua conta: "))
        valor= float(input("Digite o valor a ser depositado: "))
        Dep=bancoVelky.depositar(n, valor)
        Saldo=bancoVelky.consultaSaldo(n)
        print("Dinheiro Depositado!\nO saldo atual da conta" , n , "é de: R$", Saldo)
    elif escolha==4:
        #Sacar da Conta
        n= int(input("Digite o número da sua conta: "))
        valor= float(input("Digite o valor a ser sacado: "))
        Sac= bancoVelky.sacar(n, valor)
        Saldo= bancoVelky.consultaSaldo(n)
        if Sac:
            print("Dinheiro Sacado!")
        else:
            print("Saldo insuficiente...\n\n\n")
        print("O saldo atual da conta" , n , "é de: R$",Saldo)
    elif escolha == 5:
        print("Rendendo Poupanca...")
        n= int(input("digite o numero da conta poupanca:"))
        rend= bancoVelky.renderPoupanca(n)
        Saldo= bancoVelky.consultaSaldo(n)
        if rend:
            print("Poupanca com novo saldo")
        else:
            print("A conta não é poupanca ou não existe")
        print("O saldo atual da conta" , n , "é de: R$", Saldo)
    escolha= int(input("Digite a opção desejada:"))