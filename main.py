"""string fixed the pylint error."""

print("Hola Mundo!!")
print("El animalito " * 4)



numero = "12345"

numero_impar = 1

for digito in numero:
    if int(digito) % 2 != 0:
        numero_impar *= int(digito)
print("El producto de los digitos impares es: ", numero_impar)
