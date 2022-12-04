quantidade= 0

for i in range(5):
    a= int(input("digite um número:"))
    if a%2 == 0:
        quantidade=quantidade+1

print("o usuário digitou", quantidade, "números pares." )
