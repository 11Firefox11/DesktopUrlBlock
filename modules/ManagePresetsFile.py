import os, pathlib, json

class PresetsFile:
    PresetsFilePath = os.path.join(pathlib.Path(os.path.realpath(__file__)).parent.parent, "dub-presets.json")

    def Load(self, name):
        pass

    @property
    def PresetsFileContent(self):
        return json.load(open(PresetsFile.PresetsFilePath,))