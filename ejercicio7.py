t = str(input("Ingresar tipo de pieza (a/b): "))

if (t != "a" and t !="b"):
    print ("el valor ingresado no es un tipo de pieza válido")

else:
    
    m = int(input("Ingresar la medida: "))
    if t=="a":
        if m >= 163 and m <= 167:
            print("Cumple con las especificaciones") 
        else:
            print("No cumple con las especificaciones")
    if t=="b":
        if m >= 177 and m <= 183:
            print("Cumple con las especificaciones")
        else:
            print("No cumple con las especificaciones")
     
