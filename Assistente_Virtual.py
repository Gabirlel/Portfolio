import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

wikipedia.set_lang("pt")

# Inicializa o motor de fala
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Ajusta a velocidade da fala

# Função para falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Função para reconhecer fala
def ouvir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        falar("Diga algo")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta o ruído ambiente
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        falar("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de voz.")
        return None

# Função para processar o comando
def processar_comando(comando):
    if "wikipédia" in comando:
        falar("O que deseja buscar na Wikipédia?")
        pergunta = ouvir()
        if pergunta != '':
            try:
                resultado = wikipedia.summary(pergunta, sentences=2, auto_suggest=False)
                falar(resultado)
            except wikipedia.exceptions.DisambiguationError as e:
                falar("Há várias opções para essa pesquisa. Seja mais específico.")
            except wikipedia.exceptions.PageError:
                falar("Não encontrei resultados para essa pesquisa.")

    elif "youtube" in comando:
        falar("Abrindo no YouTube...")
        pesquisa = comando.replace("youtube", "")
        pywhatkit.playonyt(pesquisa)

    elif "fechar" in comando:
        falar("Desligando assistente.")
        exit()

    else:
        falar("Comando não reconhecido.")

# Loop principal
if __name__ == "__main__":
    falar("Olá, como posso ajudar?")
    while True:
        comando_usuario = ouvir()
        if comando_usuario:
            processar_comando(comando_usuario)

