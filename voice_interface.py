import speech_recognition as sr
from gtts import gTTS
import requests
import os

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)

def send_to_rasa(message):
    response = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"sender": "user", "message": message})
    return response.json()[0]["text"]

def speak_response(response_text):
    tts = gTTS(response_text, lang='en')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")

if __name__ == "__main__":
    user_input = capture_voice()
    bot_response = send_to_rasa(user_input)
    speak_response(bot_response)



