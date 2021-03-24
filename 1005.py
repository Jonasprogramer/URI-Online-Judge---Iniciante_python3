A = float(input())
B = float(input())

if(A >= 0 and A <= 10.0) and (B >= 0 and B <= 10.0):
    MEDIA = ((A * 3.5) + (B * 7.5)) / 11 #calculo da média ponderada nota * peso / soma dos pesos
    print('MEDIA = {:.5f}'.format(MEDIA))
else:
    print('Erro')