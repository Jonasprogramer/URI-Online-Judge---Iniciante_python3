A = float(input())
B = float(input())
C = float(input())

if(A >= 0 and A <= 10.0) and (B >= 0 and B <= 10.0) and (C >= 0 and C <= 10.0):
    MEDIA = ((A * 2) + (B * 3) + (C * 5)) /  10
    print('MEDIA = {:.1f}'.format(MEDIA))
else:
    print('Presentation Error')