# 

class Producto:
    def __init__(self, nombre: str, precio: float):
        if precio <= 0:
            raise ValueError("El precio debe ser positivo")
        self.nombre = nombre
        self.precio = precio
