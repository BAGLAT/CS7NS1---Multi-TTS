#pip install gTTS
from gtts import gTTS 
import os
import random

with open('symbols.txt', 'r') as file:
    symbols = file.read().replace('\n', '')

for j in range(100000):
  k = ''
  for k in range(8):
    k = k + str(symbols[random.randint(0,len(symbols)-1)])
  mytext = k
  language = 'en'
  myobj = gTTS(text=mytext, lang=language, slow=False) 
  myobj.save("audio_captchas/"+k+".mp3")
  if j % 300 == 0:
    print(str(j)+' done')