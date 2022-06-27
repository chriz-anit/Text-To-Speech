from gtts import gTTS    #library for Google Text-to-Speech
import os       #to open audio file automatically after its created


f = open("text.txt")

#text = "Hello world"
text = f.read()
language = "en"     #English language

obj = gTTS(text = text, lang= language, slow=False)

obj.save("sample.mp3")

os.system("sample.mp3")     #to launch mp3 player after conversion is done