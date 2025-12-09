import sounddevice as sd
import numpy as np
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

def ouvir_microfone(fs=16000, duracao=5):
    """Grava áudio por alguns segundos usando sounddevice"""
    print(f"Gravando por {duracao} segundos...")
    audio = sd.rec(int(fs * duracao), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    audio_bytes = audio.tobytes()
    audio_data = sr.AudioData(audio_bytes, fs, 2)

    r = sr.Recognizer()
    try:
        frase = r.recognize_google(audio_data, language="pt-BR")
        print("Você disse:", frase)
        return frase
    except sr.UnknownValueError:
        print("Não entendi")
    except sr.RequestError as e:
        print("Erro na requisição:", e)
    return None

def interpretar_comando(frase, comandos):
    frase = frase.lower()

    # Adicionar novo comando
    if "adicionar comando" in frase:
        chave = frase.split("adicionar comando", 1)[1].strip()
        print(f"Você pediu para adicionar: {chave}")
        if chave in comandos:
            print(f"O comando '{chave}' já existe.")
        else:
            comando = input(f"Digite o comando do sistema para '{chave}': ")
            comandos[chave] = comando
            salvar_comandos(comandos)
            print(f"Novo comando adicionado: {chave}")
        return False

    # Executar comandos existentes
    for chave, comando in comandos.items():
        if chave in frase:
            os.system(comando)
            if chave == "fechar":
                return True
            return False

    # Tentar abrir programa pelo nome
    palavras = frase.split()
    for palavra in palavras:
        if abrir_programa(palavra):
            print(f"Programa '{palavra}' aberto com sucesso!")
            return False

    print("Não encontrei programa correspondente.")
    return False

if __name__ == "__main__":
    comandos = carregar_comandos()
    while True:
        frase = ouvir_microfone()
        if not frase:
            continue
        if interpretar_comando(frase, comandos):
            break
