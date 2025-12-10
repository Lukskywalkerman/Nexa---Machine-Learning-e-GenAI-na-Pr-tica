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

## 🚀 Funcionalidades

- 🕒 **Hora atual** → "Tina que horas são"
- 📚 **Pesquisa na Wikipédia** → "Tina pesquise sobre inteligência artificial"
- 🎵 **Tocar músicas no YouTube** → "Tina toque música do Queen"
- 😂 **Contar piadas** → "Tina conte uma piada"
- 🌦️ **Clima (placeholder)** → "Tina qual a previsão do tempo"
- 🌍 **Tradução automática** (via `deep-translator`) → "Tina traduza bom dia para inglês"
- 💻 **Abrir aplicativos locais** → "Tina abra o navegador", "Tina abra o Spotify"
- 🖥️ **Controle do sistema** → "Tina desligue o computador", "Tina reinicie"
- 📝 **Notas rápidas** → "Tina anote reunião amanhã às 10h"
- 📰 **Notícias em tempo real** → "Tina últimas notícias de tecnologia"
- ❌ **Encerrar assistente** → "Tina encerrar assistente"
---

## 🔹 Fluxo de funcionamento

```text
🎤 Microfone
      │
      ▼
🧠 Reconhecimento de fala (SpeechRecognition)
      │
      ▼
⚙️ Execução de Comando (Sistema / Apps / Sites)
      │
      ▼
💬 Resposta / Ação realizada

```
---

## 🔹Lista de dependências:

speechrecognition → reconhecimento de voz via Google API

sounddevice → gravação de áudio pelo microfone

soundfile → suporte para manipulação de áudio

numpy → manipulação de arrays de áudio

requests → integração futura com APIs (ex.: Rasa)

## 🔹 Como usar
Clone este repositório:

```bash
git clone https://github.com/seuusuario/assistente-voz](https://github.com/Lukskywalkerman/Nexa---Machine-Learning-e-GenAI-na-Pr-tica/tree/main/Assistente%20de%20Voz.git
cd Assistente de Voz
```

## 🔹 Dependências
Instale as bibliotecas necessárias no Python 3.13:

```bash
pip install -r requirements.txt
```

## 🔹 Baixe o modelo de português do spaCy
```bash
python -m spacy download pt_core_news_sm
```

## 🔹Execute o programa:

```bash
python main.py
```

## 🛠️ Tecnologias usadas
- Python 3.13
- SpeechRecognition – reconhecimento de voz
- pyttsx3 – síntese de voz
- wikipedia – consultas rápidas
- pywhatkit – tocar músicas no YouTube
- pyaudio – captura de áudio
- spaCy – NLP
- deep-translator – tradução automática
- requests + BeautifulSoup4 – notícias em tempo real


## 🔹 Exemplos de comandos
- 📸 **"abrir fotos"** → abre o app Fotos  
- ⏰ **"abrir relógio"** → abre o Relógio  
- 🎵 **"adicionar comando spotify"** → você digita o caminho/execução e o comando fica salvo no JSON  

