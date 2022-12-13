def valorPagamento(valor, dias):
    juros = 0
    if dias == 0:
        return valor
    else:
        juros = 0.1 * dias

        return valor + ((3 * valor)/100) + juros 

total= 0
cont= 0
valor = float(input('Digite o valor da prestação: '))
while valor!=0 and valor>0:
    if valor!=0 and valor>0:
        dias = int(input('Digite o número de dias em atraso: '))
        total =total + valorPagamento(valor, dias)
        print("O valor a ser pago é de: ", valorPagamento(valor, dias))
        cont += 1
    valor = float(input('Digite o valor da prestação: '))

print('Quantidade total: %d' % cont)
print('Valor total das prestações: %.2f' % total)