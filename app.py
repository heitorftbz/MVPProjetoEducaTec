import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

st.set_page_config(page_title="PDTIC - MEC Digital", layout="wide")

# ---------------------------
# MENU LATERAL
# ---------------------------
st.sidebar.title("📘 PDTIC - MEC Digital")
menu = st.sidebar.radio(
    "Escolha um módulo:",
    [
        "🏠 Início",
        "🌐 Portal MEC Digital",
        "📊 Repositório de Dados Abertos",
        "☁️ Nuvem Híbrida",
        "🛡️ Centro de Operações de Segurança (SOC)"
    ]
)

# ---------------------------
# INÍCIO
# ---------------------------
if menu == "🏠 Início":
    st.title("📘 Painel MVP - PDTIC MEC 2025–2028")
    st.markdown("""
    Este protótipo (MVP) foi desenvolvido como parte do **Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC)** do MEC.

    **Objetivo:** Demonstrar, de forma simplificada, os módulos previstos no PDTIC:
    - Portal MEC Digital  
    - Repositório de Dados Abertos  
    - Nuvem Híbrida  
    - Centro de Operações de Segurança (SOC)

    ---
    """)

    st.success("Selecione um módulo no menu lateral para começar!")

# ---------------------------
# PORTAL MEC DIGITAL
# ---------------------------
elif menu == "🌐 Portal MEC Digital":
    st.title("🌐 Portal MEC Digital - MVP")
    st.subheader("Simulação de acesso unificado aos serviços educacionais")

    tab1, tab2 = st.tabs(["🔑 Login/Cadastro", "📋 Serviços Disponíveis"])

    with tab1:
        st.write("### Acesso ao sistema")
        opcao = st.radio("Escolha uma opção:", ["Login", "Cadastro"])

        if opcao == "Login":
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            if st.button("Entrar"):
                st.success(f"Bem-vindo ao MEC Digital, {email}!")
        else:
            nome = st.text_input("Nome completo")
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            if st.button("Cadastrar"):
                st.success(f"Usuário {nome} cadastrado com sucesso!")

    with tab2:
        st.write("### Serviços Educacionais Unificados")
        servicos = {
            "Consulta de Histórico Escolar": "Disponível",
            "Solicitação de Diploma Digital": "Em desenvolvimento",
            "Acesso ao ENEM Digital": "Disponível",
            "Atualização de Cadastro Educacional": "Disponível",
            "Portal de Bolsas e Financiamentos (FIES, PROUNI)": "Em desenvolvimento"
        }
        df_servicos = pd.DataFrame(list(servicos.items()), columns=["Serviço", "Status"])
        st.dataframe(df_servicos, use_container_width=True)

# ---------------------------
# REPOSITÓRIO DE DADOS ABERTOS
# ---------------------------
elif menu == "📊 Repositório de Dados Abertos":
    st.title("📊 Repositório de Dados Abertos")
    st.subheader("Bases públicas de educação")

    st.write("Faça upload de uma base CSV para visualização:")
    arquivo = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

    if arquivo:
        df = pd.read_csv(arquivo)
        st.write("### Prévia dos Dados:")
        st.dataframe(df.head(), use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.write("### Estatísticas Gerais")
            st.write(df.describe())

        with col2:
            st.write("### Gerar Gráfico")
            colunas = df.columns.tolist()
            coluna_x = st.selectbox("Eixo X", colunas)
            coluna_y = st.selectbox("Eixo Y", colunas)
            if st.button("Exibir Gráfico"):
                st.line_chart(df[[coluna_x, coluna_y]])

# ---------------------------
# NUVEM HÍBRIDA
# ---------------------------
elif menu == "☁️ Nuvem Híbrida":
    st.title("☁️ Nuvem Híbrida - Monitoramento Piloto")
    st.subheader("Simulação de desempenho e segurança")

    cpu = random.randint(30, 90)
    memoria = random.randint(40, 95)
    rede = random.randint(20, 80)

    st.metric("Uso de CPU (%)", cpu)
    st.metric("Uso de Memória (%)", memoria)
    st.metric("Tráfego de Rede (%)", rede)

    progresso = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progresso.progress(i + 1)
    st.success("Monitoramento concluído!")

    st.write("### Backup e Testes de Segurança")
    if st.button("Executar Backup"):
        st.info("Realizando backup...")
        time.sleep(2)
        st.success("Backup concluído com sucesso!")

    if st.button("Executar Teste de Segurança"):
        st.warning("Testando vulnerabilidades...")
        time.sleep(2)
        st.success("Nenhuma vulnerabilidade crítica encontrada!")

# ---------------------------
# SOC (CENTRO DE OPERAÇÕES DE SEGURANÇA)
# ---------------------------
elif menu == "🛡️ Centro de Operações de Segurança (SOC)":
    st.title("🛡️ SOC - Centro de Operações de Segurança")
    st.subheader("Registro e monitoramento de incidentes")

    if "incidentes" not in st.session_state:
        st.session_state["incidentes"] = []

    with st.form("novo_incidente"):
        tipo = st.selectbox("Tipo de incidente", ["Phishing", "Acesso não autorizado", "Malware", "Outro"])
        descricao = st.text_area("Descrição do incidente")
        enviado = st.form_submit_button("Registrar incidente")
        if enviado:
            st.session_state["incidentes"].append({
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Tipo": tipo,
                "Descrição": descricao,
                "Status": "Aberto"
            })
            st.success("Incidente registrado com sucesso!")

    st.write("### Ocorrências Registradas")
    if st.session_state["incidentes"]:
        df_inc = pd.DataFrame(st.session_state["incidentes"])
        st.dataframe(df_inc, use_container_width=True)
    else:
        st.info("Nenhum incidente registrado ainda.")

    if st.button("Emitir Alerta Simulado"):
        st.error("⚠️ Alerta: tentativa de acesso não autorizado detectada!")

# ---------------------------
# Rodapé
# ---------------------------
st.sidebar.markdown("---")
st.sidebar.caption("Desenvolvido como projeto acadêmico com base no PDTIC MEC 2025–2028.")
