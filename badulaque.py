import os
from inventario import array_frutas
from inputs import elegir_fruta, pedir_cantidad_kilos, comprar_mas_fruta
import config

def badulaque():
    """
    Ejecuta el programa para que el usuario compre frutas.
    """
    fin_de_programa = False
    precio_total = 0

    while not fin_de_programa:
        opcion_valida = False
        
        resultado = elegir_fruta(opcion_valida, array_frutas, config.array_opciones)

        if resultado is None:
            fin_de_programa = True
            continue

        nombre_fruta, precio_fruta = resultado

        cantidad_invalida = False
        precio_total = pedir_cantidad_kilos(cantidad_invalida, nombre_fruta, precio_fruta, precio_total)
        
        mas_fruta_valida = False
        if comprar_mas_fruta(mas_fruta_valida):
            continue
        else:
            fin_de_programa = True

    os.system("cls")
    print(F"\nPRECIO TOTAL: {precio_total} €\n")