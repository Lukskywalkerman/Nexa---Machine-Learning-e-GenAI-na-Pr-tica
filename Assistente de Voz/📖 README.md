# 📖 README.md — Assistente de Voz em Python
🔹 Sobre o projeto
Este projeto é um assistente de voz em Python que reconhece comandos falados em português e executa ações no computador, como abrir aplicativos ou sites. Ele utiliza SpeechRecognition com a API do Google para transcrição de voz e um catálogo de comandos em comandos.json para personalização.

🔹 Funcionalidades
🎤 Captura áudio pelo microfone usando sounddevice.

🧠 Reconhece fala em português com speech_recognition.

⚙️ Executa comandos do sistema (abrir apps, sites, etc.).

📂 Permite adicionar novos comandos dinamicamente via voz.

💾 Salva comandos personalizados em comandos.json.

🔹 Dependências
Instale as bibliotecas necessárias com:

bash
python -m pip install speechrecognition sounddevice soundfile numpy requests
Lista de dependências
speechrecognition → reconhecimento de voz via Google API.

sounddevice → gravação de áudio pelo microfone.

soundfile → suporte para manipulação de áudio.

numpy → manipulação de arrays de áudio.

requests → integração futura com APIs (ex.: Rasa, se desejar).

🔹 Como usar
Clone este repositório:

bash
git clone https://github.com/seuusuario/assistente-voz.git
cd assistente-voz
Instale as dependências:

bash
python -m pip install -r requirements.txt
Execute o programa:

bash
python main.py
Fale um comando, por exemplo:

“abrir fotos” → abre o app Fotos.

“abrir relógio” → abre o Relógio.

“adicionar comando spotify” → você digita o caminho/execução e o comando fica salvo no JSON.