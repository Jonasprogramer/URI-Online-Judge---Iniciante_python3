nome = input()
sal = float(input())
vendas_mes = float(input())

acrescimo = vendas_mes * 15 / 100
print('TOTAL = R$ {:.2f}'.format(sal + acrescimo))