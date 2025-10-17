from app.facturacion import calcular_factura

def test_calcular_factura_valores_normales():
    resultado = calcular_factura(100)
    assert resultado["subtotal"] == 100.00
    assert resultado["iva"] == 13.00
    assert resultado["total"] == 113.00

def test_calcular_factura_redondeo():
    resultado = calcular_factura(99.999)
    assert resultado["subtotal"] == 100.00  # redondea
    assert resultado["iva"] == 13.00
    assert resultado["total"] == 113.00

def test_calcular_factura_cero():
    resultado = calcular_factura(0)
    assert resultado["subtotal"] == 0.00
    assert resultado["iva"] == 0.00
    assert resultado["total"] == 0.00

def test_calcular_factura_valor_negativo():
    resultado = calcular_factura(-50)
    assert resultado["subtotal"] == -50.00
    assert resultado["iva"] == -6.50
    assert resultado["total"] == -56.50
