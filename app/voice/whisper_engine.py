import subprocess


class WhisperEngine:


    def __init__(self):

        self.exe = (
        "models/whisper/whisper-cli.exe"
        )

        self.model = (
        "models/whisper/ggml-base.en.bin"
        )


    def transcribe(self,file):

        result = subprocess.run(
        [
            self.exe,
            "-m",
            self.model,
            "-f",
            file
        ],
        capture_output=True,
        text=True
        )

        return result.stdout
