import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS


# sender = input("What is your name?\n")

bot_message = ""
message=""

#r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

#print("Bot says, ",end=' ')
#for i in r.json():
#    bot_message = i['text']
#    print(f"{bot_message}")

#myobj = gTTS(text=bot_message)
#myobj.save("welcome.mp3")
#print('saved')
# Playing the converted file
#subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("welcome.mp3")
    print('saved')
    # Playing the converted file
    subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

#def speech_to_text(input):
 #   a = input
 #  final = sr.recognizer(a)
  #  return final

#def text_to_speech(input):
   # text = input
   # final = tts(text)
    #return final
 
#def (/stt):
   # input = f.get_request('from_frontend')
    #message = speech_to_text(input)
    #r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    #speech = text_to_speech(r)

    #return render_template('index.html', r, speech)

    
