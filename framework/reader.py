from configparser import ConfigParser
import os

class Reader:
    DEFAULT_PATH = "./var/opt/kaspersky/config.ini"

    def __init__(self, config_path=None):
        self.path = config_path or os.getenv("CONFIG_PATH", self.DEFAULT_PATH)
        self.config = ConfigParser()
        self.config.read(self.path)

    def get(self, section, param):
        return self.config.get(section, param)

    def __str__(self):
        config_dict = {s: dict(self.config.items(s)) for s in self.config.sections()}
        return str(config_dict)
