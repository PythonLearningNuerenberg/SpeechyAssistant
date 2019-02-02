from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

import time
import pyaudio
import wave
import os
#
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

class StartScreen(GridLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.rows = 2
        self.add_widget(Label(text='This is a test program'))

        self.start_button = Button(text="Start Recording")
        self.start_button.bind(on_press=self.click_start_button)
        self.add_widget(self.start_button)
        #
        # self.stop_button = Button(text="Stop Recording")
        # self.stop_button.bind(on_press=self.click_stop_button)
        # self.add_widget(self.stop_button)

    def click_start_button(self,instance):
        print ("auth called")
        if not os.path.exists('./temp/'):
            os.makedirs('./temp/')

        # while self.state_recording:
        #     print('Record')

        WAVE_OUTPUT_FILENAME = "temp/output.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()


        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


class MyApp(App):
    def build(self):
        return StartScreen()


if __name__ == '__main__':
    MyApp().run()
