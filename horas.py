horaI=int(input("Qual a hora de inicio do jogo?"))
horaF=int(input("Qual a hora de fim do jogo?"))
minI= int(input("Qual o minuto de inicio do jogo?"))
minF= int(input("Qual o minuto de fim do jogo?"))
horaT= horaF - horaI
minT= minF - minI

if (horaT<0):
    horaT= 24 +  (horaF-horaI)

if (minT<0):
    minT= 60 + (minF-minI)
    horaT=horaT-1

if (horaI == horaF and minI== minF):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU "+ horaT + " HORA(S) E " + minT + " MINUTO(S)")
