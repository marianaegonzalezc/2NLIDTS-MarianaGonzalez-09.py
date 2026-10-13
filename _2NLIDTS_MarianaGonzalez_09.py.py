from typing import Optional

class Nodo:
    def __init__(self, dato: int):
        self.dato = dato
        self.siguiente: Optional[Nodo] = None

def agregar_nodo(cabeza: Optional[Nodo], valor: int) -> Nodo:
    """Agrega un nodo al final de la lista y devuelve la cabeza."""
    nuevo_nodo = Nodo(valor)

    # Si la lista está vacía, el nuevo nodo será la cabeza.
    if cabeza is None:
        return nuevo_nodo

    # Recorremos hasta llegar al último nodo.
    actual = cabeza
    while actual.siguiente is not None:
        actual = actual.siguiente

    # Enlazamos el último nodo con el nuevo.
    actual.siguiente = nuevo_nodo

    return cabeza

def imprimir_lista(cabeza: Optional[Nodo]) -> None:
    """Muestra todos los valores almacenados en la lista."""
    posicion_actual = cabeza

    print("Los valores de la lista son:", end=" ")

    while posicion_actual is not None:
        print(posicion_actual.dato, end=" ")
        posicion_actual = posicion_actual.siguiente

    print()  # Salto de línea final

def borrar_lista(cabeza: Optional[Nodo]) -> None:
    """
    Desconecta los nodos de la lista.

    Python libera automáticamente la memoria mediante el recolector de basura,
    por lo que no usamos 'delete' como en C++.
    """
    contador = 0

    while cabeza is not None:
        siguiente = cabeza.siguiente
        valor_borrado = cabeza.dato

        # Desconectamos el nodo actual de la lista.
        cabeza.siguiente = None

        print(f"Elemento borrado #{contador}: {valor_borrado}")

        cabeza = siguiente
        contador += 1

def leer_entero(mensaje: str) -> int:
    """Solicita un número entero hasta que el usuario escriba uno válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("[!] Debes ingresar un número entero.")

def main() -> None:
    cabeza: Optional[Nodo] = None

    print("[*] Actividad 09 - Lista Enlazada Simple\n")

    tamano_lista = leer_entero(
        "[+] Ingrese la cantidad de elementos a agregar a la lista: "
    )

    if tamano_lista <= 0:
        print("[!] Cantidad no válida de elementos.")
        return

    for cantidad_elementos in range(tamano_lista):
        valor = leer_entero(
            f"Ingrese el valor {cantidad_elementos + 1}: "
        )

        # Se agrega el nuevo nodo a la lista.
        cabeza = agregar_nodo(cabeza, valor)

    print()
    imprimir_lista(cabeza)

    print("\nEliminando elementos de la lista:")
    borrar_lista(cabeza)

    # La lista ya no tiene elementos.
    cabeza = None

if __name__ == "__main__":
    main()