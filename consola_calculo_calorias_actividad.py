from consola_calculo_calorias_reposo import *

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    return calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*valor_actividad
