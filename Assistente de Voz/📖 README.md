# 🎤 Assistente de Voz em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-Google%20API-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🔹 Sobre o projeto
Este projeto é um **assistente de voz em Python** que reconhece comandos falados em português e executa ações no computador, como abrir aplicativos ou sites.  
Ele utiliza **SpeechRecognition** com a API do Google para transcrição de voz e um catálogo de comandos em `comandos.json` para personalização.

---

## 🔹 Funcionalidades
- 🎤 Captura áudio pelo microfone usando **sounddevice**  
- 🧠 Reconhece fala em português com **speech_recognition**  
- ⚙️ Executa comandos do sistema (abrir apps, sites, etc.)  
- 📂 Permite adicionar novos comandos dinamicamente via voz  
- 💾 Salva comandos personalizados em `comandos.json`  

---

## 🔹 Dependências
Instale as bibliotecas necessárias com:

```bash
python -m pip install speechrecognition sounddevice soundfile numpy requests
