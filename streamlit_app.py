import streamlit as st
import google.generativeai as genai

# 1. SUA CHAVE DE ACESSO (MANTENHA EXATAMENTE ASSIM)
GOOGLE_API_KEY = "AIzaSyAYnWiouYLCYHPZHHxImqpnMyHDE5j16-4"
genai.configure(api_key=GOOGLE_API_KEY)

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Vitrine Imobiliária IA", layout="wide")

# --- MENU LATERAL (A ESTRUTURA QUE VOCÊ DEFINIU) ---
st.sidebar.title("🏗️ Painel do Corretor")
menu = st.sidebar.radio("Navegação", 
    ["📊 Dashboard", "➕ Cadastrar Imóvel", "🖼️ Gerenciador de Imóveis", "📱 Minha Vitrine (Bio)"])

# --- 1. DASHBOARD (RESUMO) ---
if menu == "📊 Dashboard":
    st.header("Resumo do seu Negócio")
    col1, col2, col3 = st.columns(3)
    col1.metric("Imóveis Ativos", "3")
    col2.metric("Visualizações", "147")
    col3.metric("Leads no WhatsApp", "12")
    
    st.markdown("---")
    st.subheader("Últimas Atividades")
    st.write("✅ Anúncio gerado para: Apartamento em Moema")
    st.write("✅ Novo lead interessado na Casa de Condomínio")

# --- 2. FORMULÁRIO DE CADASTRO INTELIGENTE ---
elif menu == "➕ Cadastrar Imóvel":
    st.header("Cadastrar Novo Imóvel")
    
    with st.form("cadastro_imovel"):
        col1, col2 = st.columns(2)
        with col1:
            titulo = st.text_input("Título do Imóvel (ex: Apto Garden)")
            tipo = st.selectbox("Tipo", ["Casa", "Apartamento", "Terreno", "Cobertura"])
        with col2:
            preco = st.text_input("Preço (R$)")
            endereco = st.text_input("Endereço Completo")
            
        tags = st.text_area("Palavras-Chave (IA): O que o imóvel tem de especial? (ex: piscina, sol da manhã, perto do metrô)")
        fotos = st.file_uploader("Upload de Fotos (Até 5)", accept_multiple_files=True)
        
        gerar_ia = st.form_submit_button("✨ SALVAR E GERAR DESCRIÇÃO COM IA")

    if gerar_ia:
        if not tags or not titulo:
            st.warning("Preencha o título e as palavras-chave para a IA trabalhar.")
        else:
            with st.spinner('A IA está criando sua descrição de luxo...'):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    prompt = f"Atue como um corretor experiente. Crie um anúncio magnético para um {tipo} chamado {titulo} que custa {preco}. Características: {tags}. Endereço: {endereco}. Termine com uma chamada para ação para o WhatsApp."
                    response = model.generate_content(prompt)
                    
                    st.success("Imóvel Cadastrado e Descrição Gerada!")
                    st.markdown("### 📝 Descrição Sugerida:")
                    st.write(response.text)
                    st.info("Esta descrição ficará visível na sua Vitrine (Bio).")
                except Exception as e:
                    st.error(f"Erro ao conectar com a IA: {e}")

# --- 3. GERENCIADOR DE IMÓVEIS ---
elif menu == "🖼️ Gerenciador de Imóveis":
    st.header("Seus Imóveis Cadastrados")
    # Simulação de lista
    col1, col2, col3 = st.columns([3, 1, 1])
    col1.write("**Apartamento Moema** - R$ 850.000")
    col2.button("Editar", key="ed1")
    col3.button("Pausar", key="p1")
    
    st.write("---")
    col1, col2, col3 = st.columns([3, 1, 1])
    col1.write("**Casa em Pinheiros** - R$ 1.500.000")
    col2.button("Editar", key="ed2")
    col3.button("Pausar", key="p2")

# --- 4. A VITRINE DO CLIENTE (O LINK DA BIO) ---
elif menu == "📱 Minha Vitrine (Bio)":
    st.header("Preview da sua Vitrine (Link da Bio)")
    st.info("É assim que seu cliente verá seu perfil no celular.")
    
    st.markdown("""
        <div style='text-align: center; background: white; padding: 20px; border-radius: 20px; border: 1px solid #ddd'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='100'>
            <h2>Corretor de Sucesso</h2>
            <p>CRECI: 12345-F</p>
            <button style='background: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 10px'>Falar no WhatsApp</button>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Imóveis em Destaque")
    st.image("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500", caption="Casa de Luxo - R$ 2.500.000")
    if st.button("Ver Detalhes do Imóvel"):
        st.write("Aqui abriria a página detalhada com a descrição que a IA criou.")
