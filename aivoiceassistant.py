import speech_recognition as sr
import pyttsx3
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm =OllamaLLM(model="mistral")

chat_history=ChatMessageHistory()

engine=pyttsx3.init()
engine.setProperty("rate",180)

recognizer=sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("\n Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
    try:
        query=recognizer.recognize_google(audio)
        print("You said :",query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry I couldnt understand")
        return ""
    except sr.RequestError:
        print("Speech Recognition Service Unavailable")
        return ""

prompt=PromptTemplate(
    input_variables=["chat_history","question"],
    template="Previous Conversation: {chat_history}\nUser: {question}\nAI:"
)

#func to process ai response
def run_chain(question):
    chat_history_text="\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
    #run ai response
    response=llm.invoke(prompt.format(chat_history=chat_history_text,question=question))
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)
    return response

speak("Hello : I am your AI Assistant. How can I help you today?")
while True:
    query=listen()
    if "exit" in query or "stop" in query:
        speak("GoodBye! Have a great day.")
        break
    if query:
        response=run_chain(query)
        print("\n AI Response : ",response)
        speak(response)

