
from gtts import gTTS
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def t2s():
    text = request.get_json()
    print(text)
    obj = gTTS(text = text, slow = False, lang = 'en')    
    obj.save('audio.wav')
    return send_file('audio.wav')
    return render_template('index.html')


if __name__ == "__main__":
    app.run() 