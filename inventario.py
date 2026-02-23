def introducir_fruta(array_frutas, nombre_fruta, precio_fruta):
    """
    Introduce frutas en el array de frutas.

    Args:
        array_frutas (list): Array de frutas.
        nombre_fruta (str): Nombre de la fruta.
        precio_fruta (float): Precio de la fruta.
    """
    fruta = {nombre_fruta : precio_fruta}
    array_frutas.append(fruta)
    

array_frutas = []

introducir_fruta(array_frutas, "Pera", 11.5)
introducir_fruta(array_frutas, "Manzana", 9.5)
introducir_fruta(array_frutas, "Aguacate", 20)
introducir_fruta(array_frutas, "Limón", 14.3)
introducir_fruta(array_frutas, "Sandía", 31.2)