# ////////// Fifth module //////////
# ////////// Speech Synthesis //////////
# ////////// Text to Speech //////////


# https://youtu.be/_Q8wtPCyMdo
# https://pypi.org/project/playsound/
# pip install gtts

from gtts import gTTS
import os
from playsound import playsound

def speechSynthesis(input_txt):
    language = "en"

    output = gTTS(text = input_txt, lang = language, slow = False)
    output.save("output.mp3")
    os.system("start output.mp3")

    playsound('output.mp3')