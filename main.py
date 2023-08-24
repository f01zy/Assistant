import speech_recognition as sr
import time
import pvporcupine
import config
import random

from pvrecorder import PvRecorder
from commands.say import say
from commands.callback import callback

r = sr.Recognizer()
m = sr.Microphone(1)

with m as source:
    r.adjust_for_ambient_noise(source)
    
porcupine = pvporcupine.create(
  access_key='/D5Sh2uqEBGiCtQ0nov0YxR8AOWA4QSeYZy9XnrPArd/AGrSpS8UAQ==',
  keyword_paths=['picovoice/Jarvis_en_windows_v2_2_0.ppn']
)

recorder = PvRecorder(device_index = 0 , frame_length = porcupine.frame_length)

print(f"Using device: {recorder.selected_device}")
print(f"{config.NAME} v{config.VER} готов к работе")

while True:
    recorder.start()
    audio = recorder.read()
    keyword_index = porcupine.process(audio)
    if keyword_index == 0:
        recorder.stop()
        say("run.wav")
        
        date = time.time()
        
        while time.time() - date <= 10:
            stop = r.listen_in_background(m , callback)
            time.sleep(10)
            stop()