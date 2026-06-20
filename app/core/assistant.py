from app.ai.ollama_client import OllamaClient


class Assistant:


    def __init__(self, config):

        self.ai = OllamaClient(
            config.get("ollama","host"),
            config.get("ollama","model")
        )


    def ask(self, message):

        prompt = f"""

You are Jarvis.

You are a helpful Windows AI assistant.

User:
{message}

Jarvis:
"""

        return self.ai.generate(prompt)
