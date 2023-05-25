k = int(input("Ingrese la cantidad de términos de Fibonacci: "))
F = [None] * (k)
I = 2
F[0] = 1
F[1] = 1
while I < k:
    F[I] = F[I-1] + F[I-2]
    I = I + 1
print(F, "Es el conjunto de los",k,"primeros números de Fibonacci")
