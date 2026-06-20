import requests


class OllamaClient:

    def __init__(self, host, model):

        self.url = host + "/api/generate"
        self.model = model


    def generate(self, prompt):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        return response.json()["response"]
