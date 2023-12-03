class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de Productos:")
        for producto in self.productos:
            print(producto)

# Ejemplo de uso
if __name__ == '__main__':
    # Crear instancias de productos
    producto1 = Producto(codigo="001", nombre="Filtro de Aceite", precio=15.99)
    producto2 = Producto(codigo="002", nombre="Batería para Auto", precio=89.99)
    producto3 = Producto(codigo="003", nombre="Pastillas de Frenos", precio=24.99)

    # Crear un catálogo y agregar productos
    catalogo = Catalogo()
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar la lista de productos en el catálogo
    catalogo.mostrar_productos()
