#SUELDO PROMEDIO
def sueldoPromedio():
    return (300+300+300+300+300+300+500+500+500+500+700+700) / 12

#FUNCION INPUT MES
def miFuncion(mes):
    while (mes.lower() != 'enero') and (mes.lower() != 'febrero') and (mes.lower() != 'marzo') and (mes.lower() != 'abril') and (mes.lower() != 'mayo') and (mes.lower() != 'junio') and (mes.lower() != 'junio') and (mes.lower() != 'agosto') and (mes.lower() != 'septiembre') and (mes.lower() != 'octubre') and (mes.lower() != 'noviembre') and (mes.lower() != 'diciembre'):
        mes = str(input('ERROR vuelva a ingresar el mes '))
    else:
        entradaMes = mes.lower()
        return entradaMes

#VARIABLES
entradaMes = miFuncion(str(input('ingrese el mes ')))
monto = int
sueldo = str

#DEFINE EL MONTO COBRADO POR JUAN
if(entradaMes == 'enero') or (entradaMes == 'febrero') or (entradaMes=='marzo') or (entradaMes=='abril') or (entradaMes=='mayo') or (entradaMes=='junio'):
    monto=300
elif(entradaMes=='junio') or (entradaMes=='agosto') or (entradaMes=='septiembre') or (entradaMes=='octubre'):
    monto=500
elif(entradaMes=='noviembre') or (entradaMes=='diciembre'):
    monto=700
else:
    miFuncion()


#DEFINE TIPO DE SUELDO
if(monto<300):
    sueldo='bajo'
elif(monto>900):
    sueldo='mejor de lo normal'
else:
    sueldo='normal'

print('Juan cobró ' + str(monto) + ' dolares en el mes de ' + entradaMes + '. Un sueldo ' + sueldo)
print('El sueldo promedio de Juan es de ' + str(sueldoPromedio()) + ' dolares lo que es, en promedio, un sueldo normal')
