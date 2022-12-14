# ////////// First module //////////
# ////////// Speech to Text //////////

# Usefull links to solve potential problems for speech recognition:
    # 1. https://github.com/Uberi/speech_recognition#the-recognizer-cant-recognize-speech-right-after-it-starts-listening-for-the-first-time
    # 2. "Could not find PyAudio; check installation"
        # 2.1. Linux: "sudo apt install python3-pyaudio"
        # 2.2. Windows: 
            # 2.2.1. "pip install pipwin" 
            # 2.2.2. "pipwin install pyaudio"

# pip3 install SpeechRecognition
import speech_recognition as sr

# List of Microphones in the computer:
# print(sr.Microphone.list_microphone_names())

def speechRecognition (): 
    # recognizes audio
    r = sr.Recognizer()

    # Initializing source to sr.Microphone
    with sr.Microphone() as source:
        print("I'm listening... ")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        #r.adjust_for_ambient_noise
        try:
            text = r.recognize_google(audio)
            #print("Your query is: {}".format(text))
            return text
        except:
            #print("Sorry could not recognize your voice!")
            return "Sorry could not recognize your voice!"
