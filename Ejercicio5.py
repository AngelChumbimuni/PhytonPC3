class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}"

    def identificar_origen(self):
        # Dividir el código en partes usando el guion como separador
        partes_codigo = self.codigo.split('-')

        # Verificar si el código tiene la estructura esperada
        if len(partes_codigo) == 3:
            pais = partes_codigo[0]
            lote = partes_codigo[1]
            # Año es la última parte del código
            año = partes_codigo[2]
            return f"País de origen: {pais}, Número de lote: {lote}, Año: {año}"
        else:
            return "Código no válido."

# Ejemplo de uso
if __name__ == '__main__':
    # Crear una instancia de la clase Producto
    producto = Producto(nombre="Producto1", codigo="PERU-0001-2023")

    # Imprimir el objeto de forma literal
    print(producto)

    # Identificar el país de origen y el número de lote
    informacion_origen = producto.identificar_origen()
    print(informacion_origen)
