from flask import Flask, make_response
import speech_recognition as sr
import json

app = Flask(__name__)
recognizer = sr.Recognizer()


@app.route('/')
def index():
    return make_response(json.dumps({"message": "Welcome to HomePage"}))


@app.route('/speechtotext')
def speech_to_text():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text_in_audio = recognizer.recognize_google(audio)
            text_in_audio = text_in_audio.lower()
            return make_response(json.dumps({
                "You Just Said": text_in_audio
            }))

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
