from consola_calculo_calorias_reposo import *


def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    return f"Para adelgazar es recomendado que consumas entre: {calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*0.8} y {calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*0.85} calorías al día."
