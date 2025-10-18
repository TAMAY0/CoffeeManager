import streamlit as st
from app.producto import Producto
from app.pedido import Pedido
from app.facturacion import calcular_factura

st.title("☕ CoffeeManager - Sistema de Pedidos")

# Inicializar pedidos en session_state
if "pedidos" not in st.session_state:
    st.session_state["pedidos"] = []

# Clientes y productos
clientes = st.session_state.get("clientes", ["Juan Pérez", "Ana Gómez", "Carlos Rojas"])
productos_disponibles = st.session_state.get("productos", {
    "Café": 10.0,
    "Tostada": 5.0,
    "Jugo": 8.0
})

# Formulario para registrar cliente
with st.expander("Registrar nuevo cliente"):
    nuevo_cliente = st.text_input("Nombre cliente")
    if st.button("Agregar cliente"):
        if nuevo_cliente and nuevo_cliente not in clientes:
            clientes.append(nuevo_cliente)
            st.session_state["clientes"] = clientes
            st.success(f"Cliente {nuevo_cliente} agregado.")
        else:
            st.warning("Cliente vacío o ya existe.")

# Formulario para registrar producto
with st.expander("Registrar nuevo producto"):
    nuevo_producto = st.text_input("Nombre producto")
    nuevo_precio = st.number_input("Precio producto", min_value=0.01)
    if st.button("Agregar producto"):
        if nuevo_producto and nuevo_producto not in productos_disponibles:
            productos_disponibles[nuevo_producto] = nuevo_precio
            st.session_state["productos"] = productos_disponibles
            st.success(f"Producto {nuevo_producto} agregado.")
        else:
            st.warning("Producto vacío o ya existe.")

# Selección para pedido
cliente = st.selectbox("Selecciona un cliente:", clientes)
productos_seleccionados = st.multiselect("Selecciona productos:", list(productos_disponibles.keys()))

if st.button("Calcular total y guardar pedido"):
    pedido = Pedido(cliente)
    for nombre in productos_seleccionados:
        pedido.agregar_producto(Producto(nombre, productos_disponibles[nombre]))

    subtotal = pedido.calcular_total()
    factura = calcular_factura(subtotal)

    st.success(f"Subtotal: {factura['subtotal']} Bs | IVA: {factura['iva']} Bs | Total: {factura['total']} Bs")

    # Guardar pedido en session_state
    st.session_state["pedidos"].append({
        "cliente": cliente,
        "productos": productos_seleccionados,
        "subtotal": factura["subtotal"],
        "iva": factura["iva"],
        "total": factura["total"]
    })

# Mostrar listado de pedidos
st.header("📋 Listado de pedidos realizados")
if st.session_state["pedidos"]:
    for i, p in enumerate(st.session_state["pedidos"], start=1):
        st.write(f"**Pedido #{i} - Cliente:** {p['cliente']}")
        for prod in p["productos"]:
            st.write(f"- {prod}: {productos_disponibles[prod]} Bs")
        st.write(f"Subtotal: {p['subtotal']} Bs | IVA: {p['iva']} Bs | Total: {p['total']} Bs")
        st.markdown("---")
else:
    st.info("No hay pedidos realizados aún.")
