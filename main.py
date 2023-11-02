import speech_recognition as sr
import re

while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Diga alguma coisa")
        audio = mic.listen(source)

        try:
            text = mic.recognize_google(audio, language="pt-BR")

            if re.search(r"\b" + "ajudar" + r"\b", format(text)):
                print("algo relacionado a ajuda")

            print(f"Você disse: {text}")
        except sr.UnknownValueError:
            print("Algo deu errado")