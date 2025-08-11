import os
import configparser

class Config:
    config = configparser.ConfigParser()
    _path = os.path.dirname(os.path.abspath(__file__))
    _config_file = os.path.join(_path, 'config.ini')
    def __init__(self):
        if not os.path.exists(self._config_file):
            with open(self._config_file, 'w') as file:
                self.config.write(file)
    def get(self,section,key):
        self.config.read(self._config_file)
        return self.config.get(section, key, fallback=None)
    def add(self, section,name, value):
        self.config.read(self._config_file)
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, name, value)
        with open(self._config_file, 'w') as configfile:
            self.config.write(configfile)