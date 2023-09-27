import os
import time
from gtts import gTTS
ttsString = ''
filePath = "ttsFiles/tts"
count = 0
while True:
    if len(os.listdir('chatText')) > 0:
        time.sleep(1)
        file = os.listdir('chatText')[0]
        with open('chatText/' + file) as text:
            for line in text.readlines():
                ttsString += line
        os.remove('chatText/' + file)
        tts = gTTS(ttsString, lang='ja')
        tts.save(filePath + str(count) + '.mp3')
        count += 1
        ttsString = ''