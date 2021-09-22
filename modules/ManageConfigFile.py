import os, pathlib, json

class ConfigFile:
    ConfigFilePath = os.path.join(pathlib.Path(os.path.realpath(__file__)).parent.parent, "dub-config.json")

    @property
    def ConfigFileContent(self):
        return json.load(open(ConfigFile.ConfigFilePath,))