from .UrlBlockExceptions import *
import os, pathlib, json, time

class PresetsFile:
    Path = os.path.join(pathlib.Path(os.path.realpath(__file__)).parent.parent, "dub-presets.json")
    JsonIndents = 4

    def Manage(self, name=None, value=None, typem="add", forcename=False):
        data = self.Content
        if typem == "add" or typem == "set":
            if forcename == True or name not in data or typem == "set":
                if value != None:
                    data[name] = value
                    self.Write(data)
                else:
                    self.Manage(name, typem="remove")
            else:
                raise AlreadyExists(name, "preset", "preset by that name already exists")
        elif typem == "remove":
            if name in data:
                del data[name]
                self.Write(data)
                return True
            else:
                raise DoesNotExists(name, "preset", "preset by that name does not exists")
        elif typem == "load":
            try:
                return self.Content[name]
            except:
                raise DoesNotExists(name, objecttype="preset name", message="preset by that name does not exists")
        elif typem == "reset":
            PresetsFile.Write(None)
            return True
        return True

    @staticmethod
    def Write(content):
        with open(PresetsFile.Path, "w+") as file:
            if content != None:
                file.write(json.dumps(content, indent=PresetsFile.JsonIndents, sort_keys=True))
            file.close()
            return True

    @property
    def Content(self):
        try:
            return json.load(open(PresetsFile.Path,))
        except FileNotFoundError:
            raise DoesNotExists(PresetsFile.Path, objecttype="path", message="preset file does not exists")
        except Exception as e:
            return {}