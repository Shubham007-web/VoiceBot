import speech_recognition as sr
from gtts import gTTS
import requests
import subprocess
import os

def capture_voice():
    recognizer = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names()
    print("Available microphones:", mic_list)

    # Select the correct microphone index from the list
    mic_index = 1  # Replace with the correct index for your microphone
    with sr.Microphone(device_index=mic_index) as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.energy_threshold = 150
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
            print("Audio captured. Processing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No input detected. Timeout occurred.")
            return None
        except sr.UnknownValueError:
            print("Could not understand the audio. Please speak clearly.")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to recognition service: {e}")
            return None

def send_to_rasa(message):
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": message}
        )
        if response.status_code == 200:
            bot_response = response.json()
            if bot_response:
                return bot_response[0].get("text", "No response from bot.")
            else:
                print("Empty response from bot.")
                return "I'm sorry, I didn't understand that."
        else:
            print(f"Error from Rasa server: {response.status_code}")
            return "Sorry, I couldn't process your request."
    except Exception as e:
        print(f"Error connecting to Rasa server: {e}")
        return "Connection error."

def speak_response(response_text):
    try:
        print("Generating TTS audio...")
        tts = gTTS(response_text, lang='en')
        tts.save("response.mp3")
        print("Audio generated successfully. Playing response...")
        
        # Use Windows Media Player or VLC to play audio
        subprocess.run(["wmplayer", "response.mp3"], check=True)
    except FileNotFoundError:
        print("Error: Media Player not found.")
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")

if __name__ == "__main__":
    while True:
        user_input = capture_voice()
        if not user_input:
            print("No valid input captured. Exiting...")
            break
        bot_response = send_to_rasa(user_input)
        if not bot_response:
            print("No response from the bot. Exiting...")
            break
        speak_response(bot_response)
