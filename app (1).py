import streamlit as st
import os

# Configuração visual do App
st.set_page_config(page_title="Calculadora Vitalis Energia", page_icon="⚡")

# --- EXIBIÇÃO DO LOGO ---
# Verifica se o arquivo do logo existe no repositório antes de tentar exibir
logo_path = "logo vitalis (5).jpg"
if os.path.exists(logo_path):
    st.image(logo_path, width=200)

st.title("⚡ Diagnóstico de Eficiência Energética Municipal")
st.markdown("---")

# --- ENTRADAS DE DADOS (Barra Lateral) ---
st.sidebar.header("Parâmetros do Município")
populacao = st.sidebar.number_input("Número de habitantes:", min_value=1, value=154000)
gasto_total = st.sidebar.number_input("Gasto total mensal (R$):", min_value=0.0, value=656000.0)

regiao_nome = st.sidebar.selectbox(
    "Escolha a região:",
    ["Norte / Nordeste", "Sudeste / Centro-Oeste", "Sul"]
)

# Mapeamento para a lógica original
regiao_map = {"Norte / Nordeste": 1, "Sudeste / Centro-Oeste": 2, "Sul": 3}
regiao_opcao = regiao_map[regiao_nome]

# --- LÓGICA DE CÁLCULO ---
if populacao < 50000:
    porte = "Pequeno"
elif populacao <= 500000:
    porte = "Médio"
else:
    porte = "Grande"

benchmarks = {
    1: {"Pequeno": 4.05, "Médio": 4.95, "Grande": 6.30},
    2: {"Pequeno": 3.60, "Médio": 4.40, "Grande": 5.60},
    3: {"Pequeno": 3.24, "Médio": 3.96, "Grande": 5.04}
}

benchmark_ideal = benchmarks[regiao_opcao][porte]
media_nacional = benchmark_ideal * 1.40
gasto_por_hab = gasto_total / populacao
prejuizo = max(0, gasto_total - (benchmark_ideal * populacao))

if gasto_por_hab <= benchmark_ideal:
    diagnostico = "Eficiente"
    cor = "green"
elif gasto_por_hab <= media_nacional:
    diagnostico = "Alerta"
    cor = "orange"
else:
    diagnostico = "Ineficiente"
    cor = "red"

# --- EXIBIÇÃO DOS RESULTADOS ---
st.subheader(f"Diagnóstico: :{cor}[{diagnostico}]")

col1, col2 = st.columns(2)
with col1:
    st.metric("Porte do Município", porte)
    st.metric("Gasto Real por Hab.", f"R$ {gasto_por_hab:.2f}")

with col2:
    st.metric("Benchmark Ideal", f"R$ {benchmark_ideal:.2f}")
    st.metric("Desvio do Ideal", f"{((gasto_por_hab/benchmark_ideal)-1)*100:+.2f}%")

if prejuizo > 0:
    st.error(f"💸 **Prejuízo financeiro mensal estimado:** R$ {prejuizo:,.2f}")
else:
    st.success("✅ O município está operando dentro da meta de eficiência!")

st.info(f"💡 Para atingir a eficiência, o gasto total deveria ser de no máximo **R$ {(benchmark_ideal * populacao):,.2f}**")

# --- SEÇÃO DE CONTATO PROFISSIONAL ---
st.markdown("---")
st.markdown(
    """
    ### 📞 Próximos Passos
    Para saber como melhorar a gestão de energia do seu município, entre em contato com a **Vitalis Energia**:
    *   **WhatsApp:** [19-997970002](https://wa.me/5519997970002)
    *   **E-mail:** [comercial@vitalisenergia.com](mailto:comercial@vitalisenergia.com)
    """
)
