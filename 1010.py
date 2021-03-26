line = input()
part = line.split()
l1 = int(part[0])
l2 = int(part[1])
l3 = float(part[2])

line2 = input()
part2 = line2.split()
l4 = int(part2[0])
l5 = int(part2[1])
l6 = float(part2[2])

tot = (l2 * l3) + (l5 * l6)
print('VALOR A PAGAR: R$ {:.2f}'.format(tot))