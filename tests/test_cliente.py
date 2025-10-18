from app.cliente import Cliente
import pytest

def test_crear_cliente():
    c = Cliente("Carlos")
    assert c.nombre == "Carlos"

def test_cliente_nombre_vacio():
    with pytest.raises(ValueError):
        Cliente("")
