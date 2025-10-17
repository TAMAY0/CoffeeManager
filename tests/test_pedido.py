from app.pedido import Pedido
from app.producto import Producto

def test_agregar_producto_y_total():
    pedido = Pedido("Ana")
    pedido.agregar_producto(Producto("Café", 10))
    pedido.agregar_producto(Producto("Jugo", 8))
    assert pedido.calcular_total() == 18
