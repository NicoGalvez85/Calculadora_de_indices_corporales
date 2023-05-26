from consola_calculo_imc import *
from consola_calculo_porcentaje_grasa import *
from consola_calculo_calorias_reposo import *

altura = float(input("Ingrese su altura (mts): "))
peso = float(input("Ingrese su peso (kg): "))
edad = int(input("Ingrese su edad: "))
genero = int(input('Ingrese "1" si es Femenino o "2" si es Masculino'))


print(f"Su indice de masa corporal es de {round(calcular_IMC(peso, altura),2)}")


if genero == 1:
    valor_genero = 0
else:
    valor_genero = 10.8

print(f"Su porcentaje de grasa corporal es de {round(calcular_porcentaje_grasa(peso, altura, edad, valor_genero),2)}")

if genero == 1:
    valor_genero = -161
else:
    valor_genero = 5

print(f"Usted, estando en reposo, consume {calcular_calorias_en_reposo(peso, altura, edad, valor_genero)}")