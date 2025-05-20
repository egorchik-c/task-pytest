from configparser import ConfigParser
import os

CONFIG_PATH: str = os.getenv("CONFIG_PATH")

class Reader:
    def __init__(self, config_path=CONFIG_PATH):
        self.path = config_path
        self.config = ConfigParser()
        self.config.read(self.path)

    def get(self, section, param):
        return self.config.get(section, param)

    def __str__(self):
        config_dict = {s: dict(self.config.items(s)) for s in self.config.sections()}
        return str(config_dict)
