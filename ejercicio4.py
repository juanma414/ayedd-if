#ingresar 3 numeros y decir si se ingresarion en orden creciente
a = float(input("ingrese el primer numero:"))
b = float(input("ingrese el segundo numero:"))
c = float(input("ingrese el tercer numero:"))
if a < b and b < c:
	print("se ingresaron en orden creciente")
else:
	print("no se ingresaron en orden creciente")
