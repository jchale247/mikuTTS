import time
from pygame import mixer
import os
mixer.init()
while True:
    if len(os.listdir('ttsFiles')) > 0:
        time.sleep(1)
        file = os.listdir('ttsFiles')[0]
        mixer.music.load("ttsFiles/" + file)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        os.remove('ttsFiles/' + file)