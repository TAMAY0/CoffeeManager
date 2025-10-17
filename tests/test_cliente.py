from app.cliente import Cliente

def test_crear_cliente():
    c = Cliente("Carlos")
    assert c.nombre == "Carlos"
