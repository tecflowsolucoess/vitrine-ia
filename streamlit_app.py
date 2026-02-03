import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Vitrine Imobiliária IA", layout="wide", initial_sidebar_state="expanded")

# --- ÁREA DE CONFIGURAÇÃO DA IA (GRATUITA) ---
GOOGLE_API_KEY = "AIzaSyAYnWiouYLCYHPZHHxImqpnMyHDE5j16-4"
genai.configure(api_key=GOOGLE_API_KEY)

# --- ESTILO CSS PARA PARECER APP DE CELULAR ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #007BFF; color: white; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.title("🏗️ Painel do Corretor")
    menu = st.radio("Navegação", ["Dashboard", "Cadastrar Imóvel", "Minha Vitrine (Bio)"])
    st.info("Plano: Free (Até 3 imóveis)")

# --- 1. DASHBOARD ---
if menu == "Dashboard":
    st.header("Seu Resumo")
    col1, col2 = st.columns(2)
    col1.metric("Imóveis Ativos", "2")
    col2.metric("Visualizações", "147")
    
    st.subheader("Imóveis Recentes")
    st.write("✅ Apto em Moema - R$ 850.000")
    st.write("✅ Casa de Condomínio - R$ 1.200.000")

# --- 2. CADASTRO INTELIGENTE (O MOTOR DO SAAS) ---
elif menu == "Cadastrar Imóvel":
    st.header("Novo Cadastro com IA")
    
    with st.container():
        titulo = st.text_input("Título do Imóvel")
        tipo = st.selectbox("Tipo", ["Casa", "Apartamento", "Terreno", "Comercial"])
        preco = st.text_input("Preço (R$)")
        tags = st.text_area("Palavras-Chave (ex: piscina, perto do metrô, ensolarado)")
        fotos = st.file_uploader("Upload de Fotos (Até 5)", accept_multiple_files=True)
        
        if st.button("✨ Gerar Descrição de Luxo com IA"):
            if not tags:
                st.warning("Coloque algumas palavras-chave para a IA trabalhar.")
            else:
                with st.spinner('A IA está escrevendo um anúncio magnético...'):
                    # Lógica da IA
                    try:
                        model = genai.GenerativeModel('gemini-pro')
                        prompt = f"Atue como um corretor de imóveis de luxo. Crie uma descrição persuasiva para um {tipo} chamado {titulo} que custa {preco}. Use estas características: {tags}. O texto deve ser curto e focado em vendas para Instagram."
                        response = model.generate_content(prompt)
                        st.success("Descrição Gerada com Sucesso!")
                        st.write(response.text)
                    except:
                        st.error("Para a IA funcionar, precisamos configurar sua Chave Grátis do Google.")

# --- 3. VITRINE DO CLIENTE (LINK DA BIO) ---
elif menu == "Minha Vitrine (Bio)":
    st.header("📱 Preview da sua Vitrine")
    st.write("---")
    st.markdown("### 🏠 Apartamento em Moema")
    st.image("https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=500", caption="R$ 850.000")
    st.write("Localizado a 10min do Shopping Ibirapuera. Este imóvel conta com acabamento fino e vista livre.")
    
    if st.button("💬 Tenho interesse (Chamar no WhatsApp)"):
        st.write("Redirecionando para o WhatsApp do Corretor...")
