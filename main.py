import os
import subprocess
from gtts import gTTS
def textToSpeechFunc(inputOfUser):
     t = gTTS(text=inputOfUser, lang_check=True, lang='en')
     t.save(savefile='tempAudio')
     try:
         # Try playing the audio using mpg123
         os.system('mpg123 -q tempAudio')
     except OSError:
         # If mpg123 is not found, use the default media player
         subprocess.call(['xdg-open', 'tempAudio'])
while True:
    x = input("Enter What You want me to Spell:  ")
    textToSpeechFunc(x)
