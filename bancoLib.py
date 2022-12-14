import random

class Conta():
    def __init__(self, numConta):
        self.num = numConta
        self.saldo = 0

    def deposito(self,valor):
        self.saldo = self.saldo + valor
    
    def saque(self, valor):
        self.saldo = self.saldo - valor
    
class Banco():
    def __init__(self, nome):
        self.nome=nome
        self.contas= []
    
    def getNome(self):
        return self.nome
    
    def criarConta(self):
        num = random.randint(0,10000)
        c= Conta(num)
        self.contas.append(c)
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
                conta.saque(grana)


