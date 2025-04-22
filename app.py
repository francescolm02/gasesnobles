import streamlit as st

# Constante universal de los gases en L·atm/mol·K
R = 0.0821

st.title("Calculadora de la Ecuación de los Gases Ideales")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.01, step=0.1)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01, step=1.0)
    moles = st.number_input("Número de moles (mol)", min_value=0.01, step=0.1)
    if st.button("Calcular Presión"):
        presion = (moles * R * temperatura) / volumen
        st.success(f"La presión es {presion:.2f} atm")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.01, step=0.1)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01, step=1.0)
    moles = st.number_input("Número de moles (mol)", min_value=0.01, step=0.1)
    if st.button("Calcular Volumen"):
        volumen = (moles * R * temperatura) / presion
        st.success(f"El volumen es {volumen:.2f} L")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.01, step=0.1)
    volumen = st.number_input("Volumen (L)", min_value=0.01, step=0.1)
    moles = st.number_input("Número de moles (mol)", min_value=0.01, step=0.1)
    if st.button("Calcular Temperatura"):
        temperatura = (presion * volumen) / (moles * R)
        st.success(f"La temperatura es {temperatura:.2f} K")

elif opcion == "Número de moles (n)":
    presion = st.number_input("Presión (atm)", min_value=0.01, step=0.1)
    volumen = st.number_input("Volumen (L)", min_value=0.01, step=0.1)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01, step=1.0)
    if st.button("Calcular Número de moles"):
        moles = (presion * volumen) / (R * temperatura)
        st.success(f"El número de moles es {moles:.2f} mol")
