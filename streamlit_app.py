import streamlit as st
import google.generativeai as genai

# 1. Configuração da Chave (Cole sua chave entre as aspas)
MINHA_CHAVE = "AIzaSyAYnWiouYLCYHPZHHxImqpnMyHDE5j16-4"

# 2. Ativando o "Cérebro" da IA
try:
    genai.configure(api_key=MINHA_CHAVE)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Erro na configuração da IA: {e}")

# 3. Visual do App
st.title("🏠 BrokerAI: Gestão e Vendas")

menu = st.sidebar.radio("Navegação", ["Gerador de Anúncios", "Catálogo"])

if menu == "Gerador de Anúncios":
    st.header("✍️ Gerador de Anúncios Magnéticos")
    detalhes = st.text_area("Descreva o imóvel (ex: 2 quartos, suite, em Moema)")
    
    if st.button("Gerar Texto para Instagram/Zap"):
        if detalhes:
            with st.spinner('Criando anúncio...'):
                try:
                    # Aqui a IA realmente trabalha
                    prompt = f"Crie um anúncio de luxo para este imóvel: {detalhes}"
                    resposta = model.generate_content(prompt)
                    st.success("Pronto!")
                    st.write(resposta.text)
                except Exception as e:
                    st.error(f"A IA deu um erro: {e}")
        else:
            st.warning("Por favor, descreva o imóvel antes.")
