N = int(input("Ingrese el tamaño de la lista: "))
A = [None] * N
B = [None] * 1
I = 0
M = 0
Band = 0
for I in range (I, N):
    A[I] = int(input(f"Ingrese los {N} valores: "))
B[0] = int(input("¿Qué número quiere buscar?: "))
while I >= 0:
    if A[I] == B[0]:
        M = I
        Band = 1
        I = I - 1
    else:
        I = I - 1
if Band == 1:
    print(f"El número {B[0]} que busca está en la posición N°{M} de la lista")
else:
    print("No se encontró el número en la lista ingresada")