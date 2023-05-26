from consola_calculo_imc import *
from consola_calculo_porcentaje_grasa import *
from consola_calculo_calorias_reposo import *
from consola_calculo_calorias_actividad import *
from consola_calculo_calorias_adelgazar import *

altura = float(input("Ingrese su altura (mts): "))
peso = float(input("Ingrese su peso (kg): "))
edad = int(input("Ingrese su edad: "))
genero = int(input('Ingrese "1" si es Femenino o "2" si es Masculino: '))
actividad = int(input("Indique su nivel de actividad semanal \n1 - poco o ningún ejercicio\n2 - ejercicio ligero (1 a 3 días a la semana)\n3 - ejercicio moderado (3 a 5 días a la semana)\n4 - deportista (6 -7 días a la semana)\n5 - atleta (entrenamientos mañana y tarde):  "))

print("-------------------------------------------------------")
print("\n")
print(f"Su indice de masa corporal es de {round(calcular_IMC(peso, altura),2)}")
print("\n")

# SE IMPLEMENTA ESTA FUNCION PARA EL % DE GRASA CORPORAL
def valor_genero1(genero):
    if genero == 1:
        return 0
    else:
        return 10.8

# SE IMPLEMENTA ESTA FUNCION PARA LOS DEMÁS CÁLCULOS QUE REQUIERAN valor_genero
def valor_genero2(genero):
    if genero == 1:
        valor_genero = -161
    else:
        valor_genero = 5
    return valor_genero

print("-------------------------------------------------------")
print("\n")
print(f"Su porcentaje de grasa corporal es de {round(calcular_porcentaje_grasa(peso, altura, edad, valor_genero1(genero)),2)} %")
print("\n")
print("-------------------------------------------------------")
print("\n")
print(f"Usted, estando en reposo, consume {round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero2(genero)),2)} calorias")

def valor_actividad(actividad):
    if actividad == 1:
        return 1.2
    elif actividad == 2:
        return 1.375
    elif actividad == 3:
        return 1.55
    elif actividad == 4:
        return 1.72
    elif actividad == 5:
        return 1.9
 
print("\n")
print("-------------------------------------------------------")
print("\n")
print(f"Su tasa metabólica basal segun su actividad física es de {round(calcular_calorias_en_actividad(peso, altura, edad, valor_genero2(genero), valor_actividad(actividad)))} calorias")
print("\n")
print("-------------------------------------------------------")
print("\n")
print(f"{consumo_calorias_recomendado_para_adelgazar(peso, altura, edad,valor_genero2(genero))}")
print("\n")