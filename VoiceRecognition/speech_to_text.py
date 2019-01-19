import speech_recognition as sr


class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text(self):
        with sr.AudioFile('testvoice/PythonTest.wav',) as source:
            audio = self.recognizer.record(source)
            self.recognizer.adjust_for_ambient_noise(source, duration=5)  # adapt to the noise
            message = None
            try:
                # languages: "de-DE", "en-GB", "en-US" ("en-US" is default)
                message = self.recognizer.recognize_google(audio, language="en")
                #message = self.recognizer.recognize_bing(audio, key=BING_KEY, language="de-DE")
                #message = self.recognizer.recognize_sphinx(audio, language="en-GB")
                print("You said: " + message)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error; {0}".format(e))

        return message


if __name__ == '__main__':
    handler = SpeechHandler()
    handler.speech_to_text()
