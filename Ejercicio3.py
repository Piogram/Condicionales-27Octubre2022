
horas = int(input("Ingrese horas trabajadas: "))
valorHora = float(input("Ingrese valor hora: "))
salarioBruto = 0
valorExtra = 0
if horas < 38 :
    salarioBruto = horas * valorHora
else: 
    salarioBruto = 37 * valorHora #Salario horas normales # 370
    horasExtra = horas - 37 # 3
    valorExtra = (valorHora*1.50) * horasExtra # 45
    
if salarioBruto > 1600:
    # print('salarioBrutoAntes: ', salarioBruto)
    # print('salarioBruto * 0.10: ', salarioBruto * 0.10)
    salarioBruto -= salarioBruto * 0.10
    
# print('salarioBruto: ', salarioBruto)
# print('valorExtra: ', valorExtra)
print('Salario Neto: ', salarioBruto + valorExtra)

    