import speech_recognition as sr
import re
import pyttsx3
import dotenv
import os

dotenv.load_dotenv()
gpt_key = os.getenv("OPENAI_KEY")
name = ""


while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.luciana")
        mic.adjust_for_ambient_noise(source)
        print("Diga alguma coisa")
        audio = mic.listen(source)

        try:
            text = mic.recognize_google(audio, language="pt-BR")

            if re.search(r"\b" + "ajudar" + r"\b", format(text)):
                engine.say("Estou aqui para ajudar")
                engine.runAndWait()
            elif re.search(r"\b" + "meu nome é" + r"\b", format(text)):
                res = re.search("meu nome é (.*)", format(text))
                name = res.group(1)
                engine.say(f"Olá, {name} Como vai?")
                engine.runAndWait()

            print(f"Você disse: {text}")
        except sr.UnknownValueError:
            print("Algo deu errado")