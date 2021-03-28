from math import sqrt, pow
line1 = input()
part1 = line1.split()
x1 = float(part1[0])
y1 = float(part1[1])

line2 = input()
part2 = line2.split()
x2 = float(part2[0])
y2 = float(part2[1])

Distancia = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print('{:.4f}'.format(Distancia))