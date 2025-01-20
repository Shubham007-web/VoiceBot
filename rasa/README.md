# Customer Support Voice Bot

## Description
A Rasa-based voice bot to handle customer queries related to EMI conversions, interest rates, and more.

## Setup Instructions

### Prerequisites
1. Install Python 3.8 or 3.9 (recommended for Rasa compatibility).
2. Install pip (comes with Python).

### Installing Required Packages (Windows Only)

#### 1. Install Rasa Framework
```bash
pip install rasa
pip install rasa-sdk
```

#### 2. Install Voice Integration Packages
```bash
pip install SpeechRecognition  # For capturing and processing voice input
pip install gTTS              # For converting text-to-speech (Google Text-to-Speech)
pip install playsound          # For playing back audio files
pip install pyaudio            # Required by SpeechRecognition for microphone input
```
> **Note**: If `pyaudio` fails to install, download the compatible `.whl` file for your Python version from [PyAudio Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
```bash
pip install path_to_downloaded_whl_file
```

#### 3. Install API Communication Package
```bash
pip install requests
```

#### 4. Optional: Enhanced Logging (Optional)
```bash
pip install loguru
```

#### 5. Optional: Testing Packages (Optional)
```bash
pip install pytest
pip install rasa-test  # For testing Rasa flows (if needed)
```

### Installing All Packages at Once
Create a `requirements.txt` file with the following content:
```plaintext
rasa
rasa-sdk
SpeechRecognition
gTTS
playsound
pyaudio
requests
loguru
pytest
```
Then install all dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project
1. Train the model:
   ```bash
   rasa train
   ```
2. Start the Rasa server:
   ```bash
   rasa run
   ```
3. Start the custom action server:
   ```bash
   rasa run actions
   ```
4. Run the voice interface:
   ```bash
   python voice_interface.py
   ```

## Troubleshooting
- **PyAudio Installation Issues**:
  If you encounter errors installing PyAudio, download the `.whl` file compatible with your Python version and install it manually:
  ```bash
  pip install path_to_downloaded_whl_file
  ```

- **Port Issues**:
  If the Rasa server or action server fails to start, ensure the ports `5005` and `5055` are not in use.
