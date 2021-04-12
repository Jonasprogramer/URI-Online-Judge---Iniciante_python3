idade_day = int(input())

ano = idade_day // 365
mes = (idade_day % 365) // 30
dia = (idade_day % 365) % 30

if(mes <= 12 and dia < 365):
    print('{} ano(s)'.format(ano))
    print('{} mes(es)'.format(mes))
    print('{} dia(s)'.format(dia))
else:
    print('ERROR!!!')