import streamlit as st

st.title("Leyes Empíricas de los Gases")

ley = st.selectbox(
    "Selecciona la ley empírica a aplicar:",
    ("Ley de Boyle (P-V)", "Ley de Charles (V-T)", "Ley de Gay-Lussac (P-T)")
)

st.markdown("Introduce los valores conocidos. Deja vacío (o escribe 0) el valor que deseas calcular.")

if ley == "Ley de Boyle (P-V)":
    st.subheader("P₁·V₁ = P₂·V₂")
    P1 = st.number_input("Presión inicial (P₁) [atm]", value=0.0)
    V1 = st.number_input("Volumen inicial (V₁) [L]", value=0.0)
    P2 = st.number_input("Presión final (P₂) [atm]", value=0.0)
    V2 = st.number_input("Volumen final (V₂) [L]", value=0.0)

    if st.button("Calcular"):
        if P1 == 0 and V1 and P2 and V2:
            P1 = (P2 * V2) / V1
            st.success(f"P₁ = {P1:.2f} atm")
        elif V1 == 0 and P1 and P2 and V2:
            V1 = (P2 * V2) / P1
            st.success(f"V₁ = {V1:.2f} L")
        elif P2 == 0 and P1 and V1 and V2:
            P2 = (P1 * V1) / V2
            st.success(f"P₂ = {P2:.2f} atm")
        elif V2 == 0 and P1 and V1 and P2:
            V2 = (P1 * V1) / P2
            st.success(f"V₂ = {V2:.2f} L")
        else:
            st.error("Debes dejar solo un campo en cero para calcularlo.")

elif ley == "Ley de Charles (V-T)":
    st.subheader("V₁/T₁ = V₂/T₂")
    V1 = st.number_input("Volumen inicial (V₁) [L]", value=0.0)
    T1 = st.number_input("Temperatura inicial (T₁) [K]", value=0.0)
    V2 = st.number_input("Volumen final (V₂) [L]", value=0.0)
    T2 = st.number_input("Temperatura final (T₂) [K]", value=0.0)

    if st.button("Calcular"):
        if V1 == 0 and V2 and T1 and T2:
            V1 = (V2 * T1) / T2
            st.success(f"V₁ = {V1:.2f} L")
        elif T1 == 0 and V1 and V2 and T2:
            T1 = (V1 * T2) / V2
            st.success(f"T₁ = {T1:.2f} K")
        elif V2 == 0 and V1 and T1 and T2:
            V2 = (V1 * T2) / T1
            st.success(f"V₂ = {V2:.2f} L")
        elif T2 == 0 and V1 and T1 and V2:
            T2 = (V2 * T1) / V1
            st.success(f"T₂ = {T2:.2f} K")
        else:
            st.error("Debes dejar solo un campo en cero para calcularlo.")

elif ley == "Ley de Gay-Lussac (P-T)":
    st.subheader("P₁/T₁ = P₂/T₂")
    P1 = st.number_input("Presión inicial (P₁) [atm]", value=0.0)
    T1 = st.number_input("Temperatura inicial (T₁) [K]", value=0.0)
    P2 = st.number_input("Presión final (P₂) [atm]", value=0.0)
    T2 = st.number_input("Temperatura final (T₂) [K]", value=0.0)

    if st.button("Calcular"):
        if P1 == 0 and P2 and T1 and T2:
            P1 = (P2 * T1) / T2
            st.success(f"P₁ = {P1:.2f} atm")
        elif T1 == 0 and P1 and P2 and T2:
            T1 = (P1 * T2) / P2
            st.success(f"T₁ = {T1:.2f} K")
        elif P2 == 0 and P1 and T1 and T2:
            P2 = (P1 * T2) / T1
            st.success(f"P₂ = {P2:.2f} atm")
        elif T2 == 0 and P1 and T1 and P2:
            T2 = (P2 * T1) / P1
            st.success(f"T₂ = {T2:.2f} K")
        else:
            st.error("Debes dejar solo un campo en cero para calcularlo.")
