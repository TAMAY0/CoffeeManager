def calcular_factura(subtotal: float) -> dict:
    iva = subtotal * 0.13
    total = subtotal + iva
    return {
        "subtotal": round(subtotal, 2),
        "iva": round(iva, 2),
        "total": round(total, 2)
    }
