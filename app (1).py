import streamlit as st

st.set_page_config(page_title="Calculadora de Eficiência Energética", layout="wide")

st.title("📊 Calculadora de Eficiência Energética Municipal")

# Sidebar inputs
st.sidebar.header("Configurações do Município")
populacao = st.sidebar.number_input("Número de habitantes", min_value=1, value=10000)
gasto_total = st.sidebar.number_input("Gasto total mensal (R$)", min_value=0.0, value=50000.0)
regiao = st.sidebar.selectbox("Região", ["Norte/Nordeste", "Sudeste/Centro-Oeste", "Sul"])

# Logic for size
if populacao < 50000:
    porte = "P"
elif populacao <= 500000:
    porte = "M"
else:
    porte = "G"

# Benchmarks (R$/hab)
benchmarks = {
    "Norte/Nordeste": {"P": 4.05, "M": 4.95, "G": 6.30},
    "Sudeste/Centro-Oeste": {"P": 3.60, "M": 4.40, "G": 5.60},
    "Sul": {"P": 3.24, "M": 3.96, "G": 5.04}
}

# Calculations
valor_benchmark = benchmarks[regiao][porte]
gasto_por_hab = gasto_total / populacao
ideal_total = valor_benchmark * populacao
prejuizo = max(0.0, gasto_total - ideal_total)

# Metrics display
col1, col2, col3 = st.columns(3)
col1.metric("Gasto por Hab.", f"R$ {gasto_por_hab:.2f}")
col2.metric("Benchmark Ideal", f"R$ {valor_benchmark:.2f}/hab")
col3.metric("Prejuízo Mensal", f"R$ {prejuizo:,.2f}")

# Diagnosis
st.subheader("Diagnóstico")
if gasto_por_hab <= valor_benchmark:
    st.success("✅ Município Eficiente: O gasto está dentro ou abaixo da meta ideal.")
elif gasto_por_hab <= (valor_benchmark * 1.4):
    st.warning("⚠️ Alerta: O gasto está acima do ideal, mas dentro da margem de tolerância.")
else:
    st.error("❌ Ineficiente: O gasto está significativamente acima do benchmark regional.")

st.divider()
st.info(f"💡 Dica: Para atingir a eficiência máxima, o gasto total do seu município não deve exceder R$ {ideal_total:,.2f} mensais.")