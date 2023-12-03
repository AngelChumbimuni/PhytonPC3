"""
2. Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador
radio. La clase “CIRCULO” debe tener un método que puede calcular el área en
utilizando el atributo radio.
"""
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

# Ejemplo de uso
if __name__ == '__main__':
    # Crear una instancia de la clase Circulo con un radio específico
    mi_circulo = Circulo(radio=5)

    # Calcular el área del círculo
    area_del_circulo = mi_circulo.calcular_area()

    # Imprimir el resultado
    print(f"El área del círculo con radio {mi_circulo.radio} es: {area_del_circulo}")
