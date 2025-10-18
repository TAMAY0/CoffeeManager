class Cliente:
    def __init__(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre
