#DEFINE TIPO DE SUELDO
def tipoDeSueldo(monto):
    if(monto<300):
        print('Éste mes Juan cobró un sueldo bajo')
        return monto
    elif(monto>900):
        print('Éste mes Juan cobró un sueldo mejor de lo normal')
        return monto
    else:
        print('Éste mes Juan cobró un sueldo normal')
        return monto

#CALCULA EL PROMEDIO
def calculaPromedio(enero, febrero, marzo, abril, mayo , junio, julio, agosto, septiembre, octubre, noviembre, diciembre):
    return ((enero+febrero+marzo+abril+mayo+junio+julio+agosto+septiembre+octubre+noviembre+diciembre) / 12)
    
#ES NUMERO? 

def esNumero(a):
    while True:    
        try:
            a = int(a)
            return a
        except ValueError:
            a = input('ERROR, ingrese un numero ')


#VARIABLES

montoEnero = esNumero(input('ingrese el monto cobrado en el mes de enero '))
tipoDeSueldo(montoEnero)
montoFebrero = esNumero(input('ingrese el monto cobrado en el mes de febrero '))
tipoDeSueldo(montoFebrero)
montoMarzo = esNumero(input('ingrese el monto cobrado en el mes de marzo '))
tipoDeSueldo(montoMarzo)
montoAbril = esNumero(input('ingrese el monto cobrado en el mes de abril '))
tipoDeSueldo(montoAbril)
montoMayo = esNumero(input('ingrese el monto cobrado en el mes de mayo '))
tipoDeSueldo(montoMayo)
montoJunio = esNumero(input('ingrese el monto cobrado en el mes de junio '))
tipoDeSueldo(montoJunio)
montoJulio = esNumero(input('ingrese el monto cobrado en el mes de julio '))
tipoDeSueldo(montoJulio)
montoAgosto = esNumero(input('ingrese el monto cobrado en el mes de agosto '))
tipoDeSueldo(montoAgosto)
montoSeptiembre = esNumero(input('ingrese el monto cobrado en el mes de septiembre '))
tipoDeSueldo(montoSeptiembre)
montoOctubre = esNumero(input('ingrese el monto cobrado en el mes de octubre '))
tipoDeSueldo(montoOctubre)
montoNoviembre = esNumero(input('ingrese el monto cobrado en el mes de noviembre '))
tipoDeSueldo(montoNoviembre)
montoDiciembre = esNumero(input('ingrese el monto cobrado en el mes de diciembre '))
tipoDeSueldo(montoDiciembre)
sueldoPromedio = calculaPromedio(montoEnero, montoFebrero, montoMarzo, montoAbril, montoMayo, montoJunio, montoJulio, montoAgosto, montoSeptiembre, montoOctubre, montoNoviembre, montoDiciembre)

#TIPO SUELDO PROMEDIO
def tipoSueldoPromedio(a):
    if(a<300):
        return 'bajo'
    elif(a>900):
        return 'mejor de lo normal'
    else:
        return 'normal'
    

print('Juan tiene un sueldo promedio de ' + str(sueldoPromedio) + ' dolares, lo que es en promedio un sueldo ' + tipoSueldoPromedio(sueldoPromedio))
