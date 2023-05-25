N = int(input("Ingrese el tamaño de la lista: "))
I = 0
Suma = 0
Z = 0
X = [None] * N
Y = [None] * N
for I in range (0, N):
    INV = 0
    X[I] = int(input("Ingrese el/los valores: "))
    A = X[I]
    C = 1
    while A > 1:
        A = A//10
        C = C + 1
    A = X[I]
    INV = 0
    while A > 0:
        INV = (INV*10)+(A%10)
        A=A//10
    if INV == X[I]:
        Y[Z] = X[I]
        Z=Z+1
    C = C - 1
    I = I + 1
Q = 0
for Q in range (0,Z):
    print (Y[Q], "es uno de los números capicua")
