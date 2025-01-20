# Customer Support Voice Bot

## Description
A Rasa-based voice bot to handle customer queries related to EMI conversions, interest rates, and more.

## Setup Instructions

### Prerequisites
1. Install Python 3.8 or 3.9 (for Rasa compatibility).
2. Install Anaconda 
### Setting Up the Virtual Environment
1. Open the Anaconda Prompt.
2. Create a new virtual environment:
   ```bash
   conda create -n voicebot_env python=3.8 -y
3. Activate the virtual environment
   ```bash
   conda activate voicebot_env
4. Ensure pip is installed:
   ```bash
   conda install pip -y
5. Install Required Libraries
   ```bash
   pip install -r requirements.txt
### Handling Special Cases
1. PyAudio Installation
   ```bash
   pip install path_to_downloaded_whl_file
2. Verify Installations
   ```bash
   pip list
   rasa --version
### Running the Project
1. Train the model:
   ```bash
   rasa train
2. Start the Rasa server
   ```bash
   rasa run
3. Start the custom action server:
   ```bash
   rasa run actions
4. Run the voice interface:
   ```bash
   python voice_interface.py









