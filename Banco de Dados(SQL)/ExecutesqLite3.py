import sqlite3

con= sqlite3.connect("bancoDeDados.db")

cursor= con.cursor()

cursor.execute('''CREATE TABLE Aluno (Matricula INTEGER PRIMARY KEY, Nome VARCHAR(40))''')
cursor.execute("INSERT INTO Aluno VALUES(10,'JOAO')")
cursor.execute("INSERT INTO Aluno VALUES(20,'VICTOR')")
con.commit()

cursor.close()
con.close()