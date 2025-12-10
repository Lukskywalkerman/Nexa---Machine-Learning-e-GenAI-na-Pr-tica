import streamlit as st
import speech_recognition as sr
import os
import json
import subprocess

ARQUIVO_COMANDOS = "comandos.json"

def carregar_comandos():
    if not os.path.exists(ARQUIVO_COMANDOS):
        return {}
    with open(ARQUIVO_COMANDOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_comandos(comandos):
    with open(ARQUIVO_COMANDOS, "w", encoding="utf-8") as f:
        json.dump(comandos, f, ensure_ascii=False, indent=4)

def abrir_programa(nome):
    try:
        os.startfile(nome)  # Windows
        return True
    except Exception:
        try:
            subprocess.Popen(nome)
            return True
        except Exception:
            return False

def ouvir_microfone():
    """Captura áudio diretamente com SpeechRecognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Estou ouvindo...")
        audio = r.listen(source)

    try:
        frase = r.recognize_google(audio, language="pt-BR")
        st.success(f"✅ Você disse: {frase}")
        return frase
    except sr.UnknownValueError:
        st.warning("🤔 Não entendi o que você disse.")
    except sr.RequestError as e:
        st.error(f"❌ Erro na requisição: {e}")
    return None

def interpretar_comando(frase, comandos):
    frase = frase.lower()

    if "adicionar comando" in frase:
        chave = frase.split("adicionar comando", 1)[1].strip()
        st.write(f"➕ Você pediu para adicionar: {chave}")
        if chave in comandos:
            st.warning(f"O comando '{chave}' já existe.")
        else:
            comando = st.text_input(f"Digite o comando do sistema para '{chave}':")
            if comando:
                comandos[chave] = comando
                salvar_comandos(comandos)
                st.success(f"Novo comando adicionado: {chave}")
        return False

    for chave, comando in comandos.items():
        if chave in frase:
            os.system(comando)
            st.info(f"🚀 Executando: {comando}")
            if chave == "fechar":
                return True
            return False

    palavras = frase.split()
    for palavra in palavras:
        if abrir_programa(palavra):
            st.success(f"Programa '{palavra}' aberto com sucesso!")
            return False

    st.warning("⚠️ Não encontrei programa correspondente.")
    return False

# ---------------------------
# Interface Streamlit
# ---------------------------
st.title("🎤 Assistente de Voz em Python")

# Inicializar histórico
if "historico" not in st.session_state:
    st.session_state.historico = []

comandos = carregar_comandos()

if st.button("🎙️ Falar comando"):
    frase = ouvir_microfone()
    if frase:
        st.session_state.historico.append(frase)  # adiciona ao histórico
        interpretar_comando(frase, comandos)

# Mostrar histórico
st.subheader("📜 Histórico de comandos")
if st.session_state.historico:
    for i, cmd in enumerate(st.session_state.historico, 1):
        st.write(f"{i}. {cmd}")
else:
    st.write("Nenhum comando reconhecido ainda.")
