import streamlit as st

st.set_page_config(page_title="Cálculo de Frete", layout="wide")

st.title("Calcular Frete Mínimo")

origem = st.text_input("Origem", placeholder="Digitar Cidade de Origem")
destino = st.text_input("Destino", placeholder="Digitar Cidade de Destino")

categoria = st.selectbox(
    "Categoria Veículo",
    ["Selecione", "Truck", "Carreta", "Bitrem", "Rodotrem"]
)

km_rodado = st.number_input("Km. Rodado", min_value=0.0)
eixos = st.number_input("Eixos", min_value=0, step=1)
retorno_vazio = st.checkbox("Calcular Retorno Vazio?")

margem = st.number_input("(%) Margem Empresa", min_value=0.0)
icms = st.number_input("(%) ICMS", min_value=0.0)
peso = st.number_input("Peso (ton)", min_value=0.0)

tipo_carga = st.selectbox(
    "Tipo Carga",
    ["Carga Geral", "Carga Refrigerada", "Carga Perigosa"]
)

if st.button("Calcular"):
    valor_base_km = 5.50
    frete = km_rodado * valor_base_km

    if retorno_vazio:
        frete *= 2

    frete += frete * (margem / 100)
    frete += frete * (icms / 100)

    st.success(f"Frete estimado: R$ {frete:,.2f}")