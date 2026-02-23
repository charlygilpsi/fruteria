def menu_opciones(array_frutas):
    """
    Muestra un menú con las frutas al usuario.

    Args:
        array_frutas (list): Array de frutas.

    Returns:
        str: Devuelve la cantidad que introduce el usuario.
    """
    print("\nBADULAQUE\n")
    print("Seleccione una fruta:\n")
    i = 0
    for fruta in array_frutas:
        i = i + 1
        for nombre, precio in fruta.items():
            print(f"{i}. {nombre} - {precio} €/Kilo")
    
    print(f"{i + 1}. Salir\n")
    
    return input("Introduzca el número de la fruta elegida: ")