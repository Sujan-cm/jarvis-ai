import subprocess
from playsound import playsound


class Piper:


    def __init__(self):

        self.exe = (
        "models/piper/piper.exe"
        )

        self.voice = (
        "models/piper/en_US-lessac-medium.onnx"
        )


    def speak(self,text):

        subprocess.run(
        [
        self.exe,
        "--model",
        self.voice,
        "--output_file",
        "voice.wav"
        ],
        input=text,
        text=True
        )

        playsound(
        "voice.wav"
        )
