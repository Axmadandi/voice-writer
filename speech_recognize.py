import speech_recognition as sr
#this is py voice writer project github/axmadandi
voice = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak .....')
    audio = voice.listen(source)
print(voice.recognize_google(audio))
