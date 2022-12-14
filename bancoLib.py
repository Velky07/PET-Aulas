import random

class Corrente():
    def __init__(self, numConta):
        self.num = numConta
        self.saldo = 0

    def deposito(self,valor):
        self.saldo = (self.saldo + valor) - (valor*0.001)
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

class Poupanca(Corrente):

    def render(self, rent):
        self.saldo= self.saldo + (self.saldo*(rent*0.01))

class Bonificada(Corrente):   
    def __init__(self, numConta):
        super().__init__(numConta)
        self.bonus = 0

    def depositaComBonus(self, valor):
        self.saldo = (self.saldo + valor) - (valor*0.001)
        self.bonus += (valor*0.001)
    
    def renderBonus(self):
        self.saldo = self.saldo + self.bonus
        self.bonus = 0 

    
class Banco():
    def __init__(self, nome):
        self.nome=nome
        self.contas= []
    
    def getNome(self):
        return self.nome
    
    def criarCorrente(self):
        num = random.randint(0, 1000)
        c= Corrente(num)
        self.contas.append(c)
        return num
    
    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    def criarBonificada(self):
        num = random.randint(0, 1000)
        b = Bonificada(num)
        self.contas.append(b)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.num==numConta:
                return conta.saldo
        return -1
    
    def depositarComDesconto(self, numConta, valor):
        for conta in self.contas:
            if conta.num == numConta and isinstance(conta, Bonificada):
                conta.depositaComBonus(valor)
                return True
            elif conta.num == numConta and isinstance(conta, (Corrente or Poupanca)):
                conta.deposito(valor)
                return True  
        return False
    
    def sacar(self, numConta, grana):
        for conta in self.contas:
            if conta.num==numConta:
                return conta.saque(grana)

    def renderPoupanca(self, numConta, rent):
        for conta in self.contas:
            if conta.num == numConta and isinstance(conta, Poupanca):
                conta.render(rent)
                return True
        return False

    def renderBonus(self, numConta):
        for i in self.contas:
            if i.num == numConta and isinstance(i, Bonificada):
                i.renderBonus()
                return True
        return False

