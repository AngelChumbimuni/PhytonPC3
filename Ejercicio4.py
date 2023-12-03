# menu.py
import os

def mostrar_menu():
    print("1. Dividir dos números")
    print("2. Salir")

def obtener_opcion():
    try:
        opcion = int(input("Selecciona una opción: "))
        return opcion
    except ValueError:
        print("Error: Ingresa un número válido.")
        return None

def mostrar_ruta_directorio():
    try:
        directorio_actual = os.getcwd()
        print(f"Directorio de trabajo actual: {directorio_actual}")
    except Exception as e:
        print(f"Error al obtener la ruta del directorio: {e}")
# menu.py
import os

def mostrar_menu():
    print("1. Dividir dos números")
    print("2. Salir")

def obtener_opcion():
    try:
        opcion = int(input("Selecciona una opción: "))
        return opcion
    except ValueError:
        print("Error: Ingresa un número válido.")
        return None

def mostrar_ruta_directorio():
    try:
        directorio_actual = os.getcwd()
        print(f"Directorio de trabajo actual: {directorio_actual}")
    except Exception as e:
        print(f"Error al obtener la ruta del directorio: {e}")


# operaciones.py
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
# main.py
from menu import mostrar_menu, obtener_opcion, mostrar_ruta_directorio
from operaciones import dividir

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            # Dividir dos números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(num1, num2)
            if resultado is not None:
                print(f"Resultado de la división: {resultado}")
        elif opcion == 2:
            # Mostrar la ruta del directorio de trabajo antes de salir
            mostrar_ruta_directorio()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
