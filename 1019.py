segundo = int(input())
second = segundo % 60 
minute = (segundo // 60) % 60 #tranformo em minutos, maior que 60 vira horas então pego o resto da divisão
hour = segundo // 3600
print('{}:{}:{}'.format(hour, minute, second))