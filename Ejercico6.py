# main.py
from package.menu import mostrar_menu, obtener_opcion, mostrar_ruta_directorio
from package.operaciones import dividir

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            # Dividir dos números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(num1, num2)
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
