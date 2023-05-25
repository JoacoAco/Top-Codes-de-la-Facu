#Dada una lista de N números x, indicar si la misma viene ordenada ascendentemente#
N = int(input("Ingrese el tamaño de la lista: "))
X = [None] * (N+1)
I = 1
Anterior = 0
B = 0
while I <= N:
    X[I] = int(input(f"Ingrese los {N} valores: "))
    A = X[I]
    if A >= Anterior:
        Anterior = X[I]
        I = I + 1
    elif A < Anterior:
        B = 1
        Anterior = X[I]
if B == 0:
    print("La lista está ordenada ascendentemente")
elif B == 1:
    print("La lista no está ordenada ascendentemente")