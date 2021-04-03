N = int(input())
print('{}'.format(N))

print('{} nota(s) de R$ 100,00'.format(N // 100))
N %= 100
print('{} nota(s) de R$ 50,00'.format(N // 50))
N %= 50
print('{} nota(s) de R$ 20,00'.format(N // 20))
N %= 20
print('{} nota(s) de R$ 10,00'.format(N // 10))
N %= 10
print('{} nota(s) de R$ 5,00'.format(N // 5))
N %= 5
print('{} nota(s) de R$ 2,00'.format(N // 2))
N %= 2
print('{} nota(s) de R$ 1,00'.format(N // 1))
