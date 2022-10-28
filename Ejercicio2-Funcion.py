def validarTriangulo(ladoA,ladoB,ladoC):
    abMayorC = ( ladoA + ladoB ) > ladoC
    bcMayorA = ( ladoB + ladoC ) > ladoA
    acMayorB = ( ladoA + ladoC ) > ladoB
    #Opcion 1
    if abMayorC and bcMayorA and acMayorB: 
        if  ladoA == ladoB == ladoC :
            return "Equilátero"
        elif ladoA != ladoB != ladoC :
            return "Escaleno"
        else: 
            return "Isósceles"   
    else:
        return "No es posible construir un triángulo a partir de los datos ingresados"
    

a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))

resultado = validarTriangulo(a,b,c)
print('resultado: ', resultado) 



    