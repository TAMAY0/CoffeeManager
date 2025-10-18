class Producto:
    def __init__(self, nombre: str, precio: float):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if precio <= 0:
            raise ValueError("El precio debe ser positivo")
        self.nombre = nombre
        self.precio = precio
