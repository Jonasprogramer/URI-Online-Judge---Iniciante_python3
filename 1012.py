from math import pow
line = input()
part = line.split()
A = float(part[0])
B = float(part[1])
C = float(part[2])

area_triangulo = (A * C) / 2
area_circulo = 3.14159 * pow(C, 2)
area_trapezio = ((A + B) / 2) * C
area_quadrado = pow(B,2)
area_retangulo = A * B

print('TRIANGULO: {:.3f}'.format(area_triangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))