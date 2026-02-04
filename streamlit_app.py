import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DA IA ---
# Substitua pelo seu código de API real
GOOGLE_API_KEY = "AIzaSyAYnWiouYLCYHPZHHxImqpnMyHDE5j16-4"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="MeuCorretor - O Braço Direito do Corretor", layout="wide")

st.title("🏠 BrokerAI: Gestão e Vendas")
st.sidebar.title("Menu de Ferramentas")
opcao = st.sidebar.radio("O que vamos fazer agora?", 
                         ["Gerador de Anúncios", "Qualificador de Leads", "Catálogo Rápido"])

# --- 1. GERADOR DE ANÚNCIOS (COM IA REAL) ---
if opcao == "Gerador de Anúncios":
    st.header("✍️ Gerador de Anúncios Magnéticos")
    detalhes = st.text_area("Descreva o imóvel (ex: 2 quartos, suite, varanda gourmet, Moema)", height=150)
    tom = st.selectbox("Tom de voz", ["Luxo/Sofisticado", "Urgência/Oportunidade", "Familiar/Aconchegante"])
    
    if st.button("Gerar Texto com IA"):
        if detalhes:
            with st.spinner('A IA está criando seu anúncio...'):
                try:
                    prompt = f"Atue como um corretor experiente. Crie um anúncio persuasivo para {tom} com base nestes detalhes: {detalhes}. Use emojis e hashtags."
                    response = model.generate_content(prompt)
                    st.success("Pronto! Aqui está o seu anúncio:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Erro ao chamar a IA: {e}")
        else:
            st.warning("Por favor, descreva o imóvel primeiro.")

# --- 2. QUALIFICADOR DE LEADS ---
elif opcao == "Qualificador de Leads":
    st.header("🎯 Qualificador de Clientes")
    st.info("Simulação: Envie este link para o cliente antes de atender no WhatsApp.")
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome do Cliente")
        renda = st.selectbox("Renda mensal aproximada", ["Até R$ 5k", "R$ 5k a 10k", "R$ 10k a 20k", "Acima de 20k"])
    with col2:
        pretensao = st.selectbox("Pretende comprar em quanto tempo?", ["Imediato", "3 a 6 meses", "Só pesquisando"])
    
    if st.button("Analisar Lead"):
        if nome:
            st.subheader("Resultado da Análise:")
            if pretensao == "Imediato" and "Acima de 10k" in renda:
                st.success(f"🔥 LEAD QUENTE: O cliente {nome} tem alto potencial. Ligue agora!")
            else:
                st.warning(f"⚡ LEAD MORNO: O cliente {nome} precisa de acompanhamento a longo prazo.")
        else:
            st.warning("Preencha o nome do cliente.")

# --- 3. CATÁLOGO RÁPIDO ---
elif opcao == "Catálogo Rápido":
    st.header("📋 Meus Imóveis Cadastrados")
    # Exemplo de mini banco de dados (simulado)
    imoveis = [
        {"Referência": "AP001", "Valor": "R$ 550.000", "Bairro": "Moema", "Status": "Disponível"},
        {"Referência": "CA002", "Valor": "R$ 1.200.000", "Bairro": "Jardins", "Status": "Reservado"},
        {"Referência": "AP003", "Valor": "R$ 320.000", "Bairro": "Itaquera", "Status": "Disponível"}
    ]
    st.table(imoveis)
    st.button("Cadastrar Novo Imóvel (Em breve)")
