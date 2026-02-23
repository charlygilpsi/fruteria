from menu import menu_opciones
from utils import cantidad_valida
import config
import os

def elegir_fruta(opcion_valida, array_frutas, array_opciones):
    """
    Muestra las frutas disponibles y pide al usuario que elija una de ellas.

    Args:
        opcion_valida (bool): Bandera que controla si la opción introducida es válida
        array_frutas (list): Array de frutas.
        array_opciones (list): Array con las opciones válidas.

    Returns:
        tuple[str, float] | None: Devuelve una tupla con el nombre y el precio de la fruta seleccionada, o None si el usuario elige salir.
    """
    while not opcion_valida:
        opcion = menu_opciones(array_frutas)
        
        if opcion not in array_opciones:
            os.system("cls")
            print("\nERROR: Introduzca una opción válida.")
            continue
        
        opcion_valida = True
        
        if int(opcion) == len(array_frutas) + 1:
            return None
        
        else:
            for nombre, precio in array_frutas[int(opcion) - 1].items():
                nombre_fruta = nombre
                precio_fruta = precio
            return nombre_fruta, precio_fruta


def pedir_cantidad_kilos(cantidad_invalida, nombre_fruta, precio_fruta, precio_total):
    """
    Pide la canitdad de kilos a comprar.

    Args:
        cantidad_invalida (bool): Bandera para comprobar que la cantidad introducida sea válida.
        nombre_fruta (str): Nombre de la fruta comrpada.
        precio_fruta (str): Precio de la fruta comprada.
        precio_total (float): Precio total de la compra.

    Returns:
        float: Precio total de la compra global.
    """
    while cantidad_invalida == False:
        cantidad = input(f"\n¿Cuánta cantidad de {nombre_fruta}? Introduzca el número: ")
        if not cantidad_valida(cantidad):
            os.system("cls")
            print("\nERROR: Introduzca una cantidad válida.")
            continue
        else:
            cantidad_invalida = True
            
        return precio_total + precio_fruta * float(cantidad)   
    

def comprar_mas_fruta(mas_fruta_valida):
    """
    Da la opción de si comprar más fruta o no.

    Args:
        mas_fruta_valida (bool): Bandera para comprobar si la respuesta es válida.

    Returns:
        bool: True si quiere comprar más y False si no.
    """
    while not mas_fruta_valida:
        mas_fruta = input("\n¿Quieres comprar más frutas? Escribe sí o no: ")
        if mas_fruta.lower() not in config.respuestas_negativas and mas_fruta.lower() not in config.respuestas_afirmativas:
            os.system("cls")
            print("\nERROR: Introduzca sí o no.")
            continue
        else:
            mas_fruta_valida = True
    
    if (mas_fruta.lower() in config.respuestas_afirmativas):
        os.system("cls")
        return True
    else:
        return False