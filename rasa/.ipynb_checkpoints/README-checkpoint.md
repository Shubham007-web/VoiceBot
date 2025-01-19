# Customer Support Voice Bot

## Description
A Rasa-based voice bot to handle customer queries related to EMI conversions, interest rates, and more.

## Setup Instructions
1. Clone this repository.
2. Install Rasa and dependencies:
   ```bash
   pip install rasa
   pip install SpeechRecognition gTTS requests
   ```
3. Train the model:
   ```bash
   rasa train
   ```
4. Run the Rasa server:
   ```bash
   rasa run
   ```
5. Run the custom action server:
   ```bash
   rasa run actions
   ```
6. Test the bot with `voice_interface.py`.
