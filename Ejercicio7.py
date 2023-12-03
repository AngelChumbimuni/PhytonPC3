class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = False  # Nuevo atributo para indicar si el teléfono está encendido o apagado

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} se ha encendido.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} se ha apagado.")

    def make_call(self, number):
        if self.is_on:
            print(f"Llamando al número {number}...")
        else:
            print("¡Enciende el teléfono antes de hacer una llamada!")

    # Nuevo método y atributos
    def set_ringtone(self, ringtone):
        self.ringtone = ringtone
        print(f"Tonos de llamada actualizado: {self.ringtone}")

# Ejemplo de uso
if __name__ == '__main__':
    my_phone = Phone(brand="Samsung", model="Galaxy S21", price=999.99)

    my_phone.turn_on()
    my_phone.make_call("123456789")
    my_phone.set_ringtone("Classic Ring")
    my_phone.turn_off()