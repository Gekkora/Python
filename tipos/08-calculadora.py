n1 = input("ingresa primer numero")
n2 = input("ingresa segundo numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
para los numeros {n1} y {n2},
el resltado de la suma es {suma}.
el resltado de la resta es {resta}.
el resltado de la multiplicacion es {multi}.
el resltado de la division es {div}.
"""

print(mensaje)
