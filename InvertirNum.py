N = int(input("Ingrese el tamaño de la lista: "))
I = 0
X = [None] * (N)
for I in range (I, N):
    X[I] = int(input("Ingrese los valores: "))
    I = I + 1
C = (N-1)
Suma = 0
while I >= 1:
    Suma = Suma + X[I-1]*(10**C)
    I = I - 1
    C = C - 1
print (Suma)
