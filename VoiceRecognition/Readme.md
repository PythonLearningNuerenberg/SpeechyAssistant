# SpeechyAssistent

In this part or group we try to built various modules for Speech Recognition (Speech-to-Text) and Natural Language Understanding (NLU).


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

1. First try to recognize speech from a wav file or microphone, using SpeechRecognition Library and various APIs. For Demo purposes we first using Google Speech Recognition. The library can use other services, too!

### Prerequisites

What things you need to install the software and how to install them

* Python3
* pip install SpeechRecognition
* pip install pyaudio  (OSX:  brew install portauto & pip3 install pyaudio )

For the demo we're using Google Speech with builtin api, for other APIs you need to generate a key

### Demo

python3 microphone_recognition.py

-> "Say something!" 

Service tries to recognize Speech Input from your active microphone input and translates to text



## Built With

* [Python 3](https://www.python.org/) 
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Library for performing speech recognition, with support for several engines and APIs, online and offline
* [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - Cross Platform audio I/O Library


## Authors

* **sherpadee** - *Initial work*

See also the list of [contributors](https://github.com/orgs/PythonLearningNuerenberg/people) who participated in this project.

## Coding Comventions

* [CodeStyle](https://docs.python-guide.org/writing/style/#code-style) - The Hitchhikers Guide to Python


## License

This project is licensed under the GNU - GPL v3

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
