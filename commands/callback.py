import config
import speech_recognition as sr

from .execute import execute
from .recognize import recognize
from .say import say

def callback(recognizer , audio):
    try:
        voice = recognizer.recognize_google(audio , language="ru-RU").lower()
        
        cmd = voice
                      
        cmd = recognize(cmd)
        execute(cmd['cmd'])  
            
    except sr.UnknownValueError:
        say("Голос не распознан!")
        
    except sr.RequestError as e:
        say("Неизвестная ошибка, проверьте интернет!")