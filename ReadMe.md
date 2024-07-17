# Assistant With UI


## Project Overview

Jarvis is a voice-activated AI assistant with a user-friendly graphical interface. This project was developed during my Python Development Internship at CodeClause. It utilizes Google's speech recognition and generative AI to understand and respond to user commands.

## Features

- **Voice Recognition**: Powered by Google's speech recognition.
- **Generative AI**: Utilizes Google's generative AI for intelligent responses.
- **Adaptive UI**: Toggle between minimized and maximized screen modes.
- **Gradient Background**: Visually appealing gradient background.
- **Interactive Elements**: Microphone button for voice input and a chatbox for displaying interactions.

## Tech Stack

- **Python**: Core development language.
- **Tkinter**: For building the graphical user interface.
- **Google Generative AI**: For generating intelligent responses.
- **Pyttsx3**: For text-to-speech conversion.

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `speech_recognition`
  - `google-generativeai`
  - `pyttsx3`
  - `Pillow`
  - `tkinter`

### Installation

1. Install the required libraries:

   ```sh
   pip install -r requirements.txt

### Running the Application

1. Navigate to the project directory:
   
    ```sh
    cd /path/to/project/directory

3. Run the application:

    ```sh
    python main.py

## How It Works

1. Voice Input: 
    * User clicks on the microphone button to speak.
    * The speech is captured using the 'speech_recognition' library.

2. Processing:
    * The captured speech is sent to Google's speech recognition API for transcription.
    * The transcribed text is processed using Google's generative AI to generate a response.

3. Response Generation:
    * The AI generates a response based on the user's input.
    * If the response contains a command to open a website, it can do so in any installed browser.

4. Voice Output:
    * The response is displayed in the chatbox.
    * The response is also read aloud using the 'pyttsx3' library for text-to-speech conversion.

## Acknowledgements
* CodeClause: For providing the internship opportunity and support.
* Google: For the powerful AI and speech recognition APIs.
* Python Community: For the amazing libraries and resources.
