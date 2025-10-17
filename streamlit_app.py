import streamlit as st
from app.producto import Producto
from app.pedido import Pedido
from app.facturacion import calcular_factura

st.title("☕ CoffeeManager - Sistema de Pedidos")

clientes = ["Juan Pérez", "Ana Gómez", "Carlos Rojas"]
productos_disponibles = {
    "Café": 10.0,
    "Tostada": 5.0,
    "Jugo": 8.0
}

cliente = st.selectbox("Selecciona un cliente:", clientes)
productos = st.multiselect("Selecciona productos:", list(productos_disponibles.keys()))

if st.button("Calcular total"):
    pedido = Pedido(cliente)
    for nombre in productos:
        pedido.agregar_producto(Producto(nombre, productos_disponibles[nombre]))

    subtotal = pedido.calcular_total()
    factura = calcular_factura(subtotal)

    st.success(
        f"Subtotal: {factura['subtotal']} Bs | IVA: {factura['iva']} Bs | Total: {factura['total']} Bs"
    )
