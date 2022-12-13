i=0
k=0
soma=0
while i>=0:
    i=int(input("Qual a sua idade?"))
    if i>=0:
        k=k+1
        soma=soma+i
else:
    print("Você encerrou o programa.")

media= soma/k

print("A média de idade dos individuos é: ",media)
