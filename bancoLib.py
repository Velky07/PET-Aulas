import random

class Corrente():
    def __init__(self, numConta):
        self.num = numConta
        self.saldo = 0

    def deposito(self,valor):
        self.saldo = self.saldo + valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

class Poupanca(Corrente):

    def render(self):
        self.saldo= self.saldo + (self.saldo*0.01)
    
class Banco():
    def __init__(self, nome):
        self.nome=nome
        self.contas= []
    
    def getNome(self):
        return self.nome
    
    def criarCorrente(self):
        num = random.randint(0,10000)
        c= Corrente(num)
        self.contas.append(c)
        return num
    
    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.num==numConta:
                return conta.saldo
        return -1
    
    def depositar(self, numConta, grana):
        for conta in self.contas:
            if conta.num==numConta:
                conta.deposito(grana)
    
    def sacar(self, numConta, grana):
        for conta in self.contas:
            if conta.num==numConta:
                return conta.saque(grana)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False

