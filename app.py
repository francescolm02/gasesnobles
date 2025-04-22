import streamlit as st

R = 0.0821  # L·atm/mol·K

st.title("Calculadora de la Ecuación de los Gases Ideales")
st.write("Ecuación: **PV = nRT**")

# Selección de variable a calcular
opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

# Mostrar inputs según la opción
if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01, format="%.4f")
    n = st.number_input("Número de moles (mol)", min_value=0.01, format="%.4f")
    T = st.number_input("Temperatura (K)", min_value=0.01, format="%.2f")
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es: {P:.4f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01, format="%.4f")
    n = st.number_input("Número de moles (mol)", min_value=0.01, format="%.4f")
    T = st.number_input("Temperatura (K)", min_value=0.01, format="%.2f")
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es: {V:.4f} L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01, format="%.4f")
    V = st.number_input("Volumen (L)", min_value=0.01, format="%.4f")
    n = st.number_input("Número de moles (mol)", min_value=0.01, format="%.4f")
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es: {T:.2f} K")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.01, format="%.4f")
    V = st.number_input("Volumen (L)", min_value=0.01, format="%.4f")
    T = st.number_input("Temperatura (K)", min_value=
