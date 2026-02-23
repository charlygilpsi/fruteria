def opciones_validas(array_frutas):
    """
    Genera un array con las opciones válidas para el menú en función de la cantidad de frutas.

    Args:
        array_frutas (list): Array de frutas.
        
    Returns:
        list: Array de opciones válidas
    """
    opciones = []
    i = 1
    for fruta in array_frutas:
        opciones.append(str(i))
        i = i + 1
    
    opciones.append(str(i))
    
    return opciones


def cantidad_valida(cantidad):
    """_summary_

    Args:
        cantidad (str): Cantidad introducida por el usuario por teclado.
    
    Returns:
        bool: True si es válida y False si no.
    """
    try:
        if float(cantidad) and float(cantidad) > 0:
            return True
    except ValueError:
        return False