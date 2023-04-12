# Configuration including a dot folder and a yaml config file

from os import path
from pathlib import Path
import yaml
from yaml import Loader

info = print
pythonpackage = "pythonpackage"


class ConfigManager:
    def __init__(self):
        self.config = None

        self.folder_path = Path.home() / f".{pythonpackage}"
        self.folder_path.mkdir(exist_ok=True)

        self.config_file = self.folder_path / "config"

    def check_config_file(self, load=False):
        if self.config_file.exists():
            with self.config_file.open(mode="r") as file:
                if load:
                    self.config = yaml.load(file.read(), Loader=Loader)
        else:
            info(f"A config file as been created in {self.folder_path}")
            self.config = {"color": "blue"}
            with self.config_file.open(mode="w") as file:
                yaml.dump(self.config, file, default_flow_style=False)

    def save(self):
        self.check_config_file()
        with self.config_file.open(mode="w") as file:
            yaml.dump(self.config, file, default_flow_style=False)

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        self.save()
