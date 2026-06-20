import sounddevice as sd
from scipy.io.wavfile import write


class Recorder:

    def __init__(self):
        self.rate = 16000


    def record(
        self,
        filename="input.wav",
        seconds=5
    ):

        print("Listening...")

        audio = sd.rec(
            int(seconds*self.rate),
            samplerate=self.rate,
            channels=1
        )

        sd.wait()

        write(
            filename,
            self.rate,
            audio
        )

        print("Recorded")

        return filename
