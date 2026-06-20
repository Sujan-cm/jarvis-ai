import yaml


class Config:

    def __init__(self):

        with open(
            "config.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            self.data = yaml.safe_load(file)


    def get(self, *keys):

        value = self.data

        for key in keys:
            value = value[key]

        return value
