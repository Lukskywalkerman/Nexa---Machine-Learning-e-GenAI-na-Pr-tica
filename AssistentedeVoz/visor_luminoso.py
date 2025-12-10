import streamlit as st
import speech_recognition as sr
import os
import json

st.set_page_config(page_title="Assistente de Voz", page_icon="🎤", layout="centered")

# Título
st.title("🎤 Assistente de Voz em Python")

# Estado do "visor luminoso"
if "listening" not in st.session_state:
    st.session_state.listening = False

# Botão para gravar áudio
if st.button("🎙️ Falar comando"):
    st.session_state.listening = True  # acende o visor

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.markdown("🟢 **Visor aceso: estou ouvindo...**")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        st.success(f"Você disse: {comando}")

        # Carregar comandos do JSON
        with open("comandos.json", "r", encoding="utf-8") as f:
            comandos = json.load(f)

        if comando in comandos:
            os.system(comandos[comando])
            st.info(f"Executando: {comandos[comando]}")
        else:
            st.warning("Comando não encontrado. Adicione no JSON.")

    except Exception as e:
        st.error(f"Erro: {e}")

    st.session_state.listening = False  # apaga o visor

# Mostrar estado do visor
if st.session_state.listening:
    st.markdown("🟢 **Visor aceso**")
else:
    st.markdown("⚪ **Visor apagado**")
