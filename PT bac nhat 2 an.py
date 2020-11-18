a, b, c = map( float, input().split())
d, e, f = map( float, input().split())

D=float(a*e-b*d);
dx=float(c*e-b*f);
dy=float(a*f-c*d);
if D==0:
    if dx+dy==0:
        print('Vo so nghiem')
    else:
        print('Vo nghiem')
else:
    x=dx/D
    y=dy/D
    print(f"{format(x, '.3f')} {format(y, '.3f')}")
