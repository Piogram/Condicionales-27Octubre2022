numero = int(input("Ingrese un número: ")) 

#Opcion 1
esPar = numero % 2 == 0
if numero == 0:
    print("Neutro")
elif esPar and numero > 0:
    print("Positivo Par")
elif not esPar and numero > 0:
    print("Positivo Impar")
elif esPar and numero < 0:
    print("Negativo Par")
elif not esPar and numero < 0:
    print("Negativo Impar")


# Opcion 2
if numero == 0:
    print("Neutro")
else:
    esPar = numero % 2 == 0
    if esPar :
        if numero > 0:
            print("Positivo par")  
        else:
            print("Negativo par")  
    else:
        if numero > 0:
            print("Positivo impar")       
        else:
            print("Negativo impar")  
               




    
    
    


    
    
