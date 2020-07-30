import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Please Speak Now..")
            audio = recognizer.listen(source)
            text_in_audio = recognizer.recognize_google(audio)
            text_in_audio = text_in_audio.lower()
            print("\n You Just Said : ", text_in_audio)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")