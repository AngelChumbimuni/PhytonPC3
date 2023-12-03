class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.edad = int(input("Ingrese la edad: "))
        self.direccion = input("Ingrese la dirección: ")

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nDirección: {self.direccion}"

# Ejemplo de uso
if __name__ == '__main__':
    # Crear una instancia de la clase Persona con datos ingresados desde el teclado
    nueva_persona = Persona()

    # Imprimir los detalles de la persona
    print("\nDetalles de la Persona:")
    print(nueva_persona)
