import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import spacy
import os
import requests
import json
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Carrega modelo de linguagem do spaCy (português)
nlp = spacy.load("pt_core_news_sm")

wake_word = "tina"
rodando = True  # controle do loop principal

# Caminho relativo ao próprio script
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "comandos.json")

with open(json_path, "r", encoding="utf-8") as f:
    comandos_apps = json.load(f)

# Intenções com exemplos
intencoes = {
    "hora": ["que horas são", "me diga a hora", "horário agora"],
    "pesquisa": ["procure por", "pesquise sobre", "quem é", "explique"],
    "musica": ["toque", "coloque música", "reproduza"],
    "piada": ["conte uma piada", "me faça rir"],
    "clima": ["qual a previsão do tempo", "vai chover hoje", "como está o clima"],
    "traducao": ["traduza", "tradução", "translate"],
    "abrir": ["abra", "inicie", "executar"],
    "sistema": ["desligue", "reinicie", "shutdown", "restart"],
    "nota": ["anote", "salve", "memorize"],
    "noticias": ["últimas notícias", "novidades", "atualizações", "news"],
    "encerrar": ["encerrar assistente", "fechar assistente", "parar tina"]
}

def detectar_intencao(frase):
    doc = nlp(frase)
    melhor_intencao = None
    melhor_score = 0
    for intent, exemplos in intencoes.items():
        for exemplo in exemplos:
            score = doc.similarity(nlp(exemplo))
            if score > melhor_score:
                melhor_score = score
                melhor_intencao = intent
    return melhor_intencao

def falar_texto(texto: str):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

def buscar_noticias():
    try:
        url = "https://www.techtudo.com.br/ultimas/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        titulos = [t.get_text() for t in soup.find_all("h2")[:5]]
        return titulos
    except Exception:
        return ["Não consegui acessar as notícias agora."]

def executar_comando(comando: str) -> str:
    global rodando
    intent = detectar_intencao(comando)
    resposta = "Ainda não sei como responder isso."

    if intent == "hora":
        hora = datetime.datetime.now().strftime("%H:%M")
        resposta = f"Agora são {hora}"

    elif intent == "pesquisa":
        buscar = comando.replace("procure por", "").replace("pesquise", "").strip()
        wikipedia.set_lang("pt")
        try:
            resposta = wikipedia.summary(buscar, sentences=2)
        except Exception:
            resposta = "Não encontrei nada na Wikipédia."

    elif intent == "musica":
        musica = comando.replace("toque", "").replace("reproduza", "").strip()
        try:
            pywhatkit.playonyt(musica)
            resposta = f"Tocando {musica} no YouTube."
        except Exception:
            resposta = "Não consegui abrir o YouTube para tocar a música."

    elif intent == "piada":
        resposta = "Por que o livro de matemática ficou triste? Porque tinha muitos problemas!"

    elif intent == "clima":
        resposta = "Ainda não sei prever o tempo, mas posso buscar na web."

    elif intent == "traducao":
        if "inglês" in comando:
            alvo = "en"
        elif "espanhol" in comando:
            alvo = "es"
        elif "português" in comando:
            alvo = "pt"
        else:
            alvo = "en"
        texto_original = comando.replace("traduza", "").replace("tradução", "").strip()
        try:
            traducao = GoogleTranslator(source="auto", target=alvo).translate(texto_original)
            resposta = f"Tradução: {traducao}"
        except Exception:
            resposta = "Não consegui traduzir agora."

    elif intent == "abrir":
        app = comando.replace("abra", "").replace("inicie", "").replace("executar", "").strip()
        if app in comandos_apps:
            caminho = comandos_apps[app]
            os.system(f'start "" "{caminho}"')
            resposta = f"Abrindo {app}..."
        else:
            resposta = f"Não encontrei o comando para '{app}' no JSON."

    elif intent == "sistema":
        if "desligue" in comando or "shutdown" in comando:
            resposta = "Desligando o computador..."
            os.system("shutdown /s /t 5")
        elif "reinicie" in comando or "restart" in comando:
            resposta = "Reiniciando o computador..."
            os.system("shutdown /r /t 5")

    elif intent == "nota":
        nota = comando.replace("anote", "").replace("salve", "").strip()
        with open("notas_tina.txt", "a", encoding="utf-8") as f:
            f.write(nota + "\n")
        resposta = f"Anotei: {nota}"

    elif intent == "noticias":
        noticias = buscar_noticias()
        resposta = "Aqui estão algumas notícias recentes:\n" + "\n".join(noticias)

    elif intent == "encerrar":
        resposta = "Encerrando a assistente. Até logo!"
        rodando = False

    else:
        resposta = f"Não entendi '{comando}', mas posso pesquisar na web."

    falar_texto(resposta)
    return resposta

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("🎙️ Ouvindo...")
        audio = r.listen(source)
        try:
            frase = r.recognize_google(audio, language="pt-BR").lower()
            return frase
        except Exception:
            return ""

# Loop principal
print("Assistente iniciada. Diga 'Tina ...' para ativar.")
while rodando:
    comando = ouvir_microfone()
    if wake_word in comando:
        comando = comando.replace(wake_word, "", 1).strip()
        resposta = executar_comando(comando)
        print("✅", resposta)
