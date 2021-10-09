from .UrlBlockExceptions import *
import os, pathlib, json

class PresetsFile:
    
    Path = os.path.join(pathlib.Path(os.path.realpath(__file__)).parent.parent, "dub-presets.json")
    JsonIndents = 4

    def Manage(self, name=None, value=None, typem="add", forcename=True):
        data = self.Content
        if typem == "add" or typem == "set":
            if forcename == True or name not in data:
                if value != None:
                    print(value)
                    if typem == "set":
                        data[name] = value
                    else:
                        print(name not in data)
                        if name not in data:
                            print("add")
                            data[name] = {}
                        for key in value:
                            data[name][key] = value[key]
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
            open(self.Path, "w+")
            return {}
        except Exception as e:
            return {}