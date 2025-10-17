from app.pedido import Pedido
from app.producto import Producto

def test_calculo_total_integrado():
    p1 = Producto("Café", 10)
    p2 = Producto("Tostada", 5)
    pedido = Pedido("Juan Pérez")
    pedido.agregar_producto(p1)
    pedido.agregar_producto(p2)
    assert pedido.calcular_total() == 15
