from app.pedido import Pedido
from app.producto import Producto
from app.facturacion import calcular_factura

def test_calculo_total_integrado():
    p1 = Producto("Café", 10)
    p2 = Producto("Tostada", 5)
    pedido = Pedido("Juan Pérez")
    pedido.agregar_producto(p1)
    pedido.agregar_producto(p2)
    assert pedido.calcular_total() == 15

def test_integracion_completa():
    p1 = Producto("Café", 10)
    p2 = Producto("Tostada", 5)
    pedido = Pedido("Juan Pérez")
    pedido.agregar_producto(p1)
    pedido.agregar_producto(p2)
    
    subtotal = pedido.calcular_total()
    factura = calcular_factura(subtotal)
    
    assert subtotal == 15
    assert factura["subtotal"] == 15
    assert factura["iva"] == 1.95
    assert factura["total"] == 16.95
