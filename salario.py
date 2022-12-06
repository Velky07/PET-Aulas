def calculaSalario(x,y,z):
    return x-(y+z)

SB=float(input("Digite o valor do salário bruto: R$"))
INSS= 0.11*SB
IR= 0.15*(SB-INSS)

Sl= calculaSalario(SB, INSS, IR)

print("Seu salário é de: R$", Sl)