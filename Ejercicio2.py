a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))

abMayorC = ( a + b ) > c
bcMayorA = ( b + c ) > a
acMayorB = ( a + c ) > b

#Opcion 1
if abMayorC and bcMayorA and acMayorB: 
    if  a == b == c : # a==b and b==c and c==a
        print("Equilátero")
    elif a != b !=c :
        print("Escaleno")
    else: # (a==b and a!=c and b!=c) or (c==b and c!=a and b!=a)  or (a==c and a!=b and c!=b)
        print("Isósceles")   
else:
    print("No es posible construir un triángulo a partir de los datos ingresados")
    
    
#Opcion 2
if abMayorC and bcMayorA and acMayorB: 
    if  a == b == c : # a==b and b==c and c==a
        print("Equilátero")
    elif (a==b and a!=c and b!=c) or (c==b and c!=a and b!=a)  or (a==c and a!=b and c!=b) :
        print("Isósceles")
    else: 
        print("Escaleno")   
else:
    print("No es posible construir un triángulo a partir de los datos ingresados")