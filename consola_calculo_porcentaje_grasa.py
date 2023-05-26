
def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):

    from consola_calculo_imc import calcular_IMC
    return 1.2 * calcular_IMC(peso,altura) + 0.23 * edad - 5.4 - valor_genero
