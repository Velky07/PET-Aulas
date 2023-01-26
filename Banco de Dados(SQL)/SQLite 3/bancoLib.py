import random
import sqlite3

con= sqlite3.connect("bandoDeDados.db")

cursor = con.cursor()

class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.con = con
        self.cursor = self.con.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Contas (Numero INTEGER PRIMARY KEY, Saldo REAL)''')
        self.con.commit()

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        self.cursor.execute(f"INSERT INTO Contas VALUES({num}, 0)")
        self.con.commit()
        return num

    def consultaSaldo(self, numConta):
        self.cursor.execute(f"SELECT Saldo FROM Contas WHERE Numero = {numConta}")
        saldo= self.cursor.fetchone()
        if saldo:
            return saldo[0]
        else:
            return -1

    def depositar(self, numConta, valor):
        self.cursor.execute(f"UPDATE Contas SET Saldo = Saldo + {valor} WHERE Numero = {numConta}")
        self.con.commit()

    def sacar(self, numConta, valor):
        self.cursor.execute(f"SELECT Saldo FROM Contas WHERE Numero = {numConta}")
        saldo = self.cursor.fetchone()
        if saldo and saldo[0] >= valor:
            self.cursor.execute(f"UPDATE Contas SET Saldo = Saldo - {valor} WHERE Numero = {numConta}")
            self.con.commit()
            return True
        else:
            return False

    def closeConnect(self):
        self.cursor.close()
        self.con.close()