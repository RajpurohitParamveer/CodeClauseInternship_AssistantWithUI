import os
import re
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
from utils import insertText

genai.configure(api_key="AIzaSyBwPdHzjkmMU94fKAHQXUwlJZGO9f_yf3Y")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

system_instruction = ("You are Jarvis, A helpful and informative AI assistant. Give short "
                      "and precise answers. Use '/c open <url> /c' to open any website in your default browser.")

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)


class GetAI:
    def __init__(self, root, status_text_var, chatbox):
        self.recog = sr.Recognizer()
        self.status_text_var = status_text_var
        self.chatbox = chatbox
        self.root = root

    def generateResponse(self):
        with sr.Microphone() as source:
            self.status_text_var.set("                 "
                                     "Listening..."
                                     "                 ")
            self.root.update_idletasks()
            audio = self.recog.listen(source, phrase_time_limit=5)

            try:
                user_input_text = self.recog.recognize_google(audio)
                insertText(self.chatbox, "You: " + user_input_text + "\n")
                self.root.update_idletasks()

                self.status_text_var.set("Thinking...")
                self.root.update_idletasks()

                convo = model.start_chat()
                convo.send_message(user_input_text)

                engine = pyttsx3.init()
                engine.setProperty('voice', 'english+f1')

                if "/c open" in convo.last.text.lower():
                    # Extract URL using regex
                    match = re.search(r'/c open (.+?) /c', convo.last.text.lower())
                    if match:
                        url = match.group(1).strip()
                        # Open URL in default browser
                        os.system(f"start {url}")
                        insertText(self.chatbox, "Jarvis: Opening " + url + " in your default browser.\n")
                    else:
                        insertText(self.chatbox, "Jarvis: I couldn't understand the URL.\n")
                else:
                    insertText(self.chatbox, "Jarvis: " + convo.last.text + "\n\n")
                    self.root.update_idletasks()
                    engine.say(convo.last.text)

                engine.runAndWait()
                self.status_text_var.set("Hi, click on the mic to speak")
                self.root.update_idletasks()

            except sr.UnknownValueError:
                self.status_text_var.set("Sorry, I did not understand that")
                self.root.update_idletasks()
            except sr.RequestError as e:
                self.status_text_var.set("Could not request results; {0}".format(e))
                self.root.update_idletasks()
            except Exception as e:
                self.status_text_var.set("An error occurred; {0}".format(e))
                self.root.update_idletasks()
