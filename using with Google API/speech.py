import speech_recognition as sr
from googletrans import Translator

r=sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration = 1)
    audio=r.listen(source)
    
try:
    text = r.recognize_google(audio)    
    print("You said : {}".format(text))
except Exception:
    pass
    print("something went wrong")
  
    
translator = Translator()
vi=translator.translate([text], dest='en')
for translation in vi:
    print(translation.text)













#r.operation_timeout =5
'''translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)'''

'''
import sys
filename=sys.argv[1]
with sr.AudioFile(filename) as source:
    audio=r.listen(source)
try:
    print("system"+r.reconize_google(audio))
except Exception:
    print("something went wrong")'''
	
#from textblob import TextBlob
#b = TextBlob(text)
#lang=b.detect_language()
