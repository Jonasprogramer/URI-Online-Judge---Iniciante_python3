line = input()
part = line.split()
v1 = int(part[0])
v2 = int(part[1])
v3 = int(part[2])

v1_v2 = ((v1 + v2) + abs(v1 - v2)) / 2
maior = ((v1_v2 + v3) + abs(v1_v2 - v3)) / 2

print('{} eh o maior'.format(int(maior)))