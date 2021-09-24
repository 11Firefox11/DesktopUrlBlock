import sys, ctypes
from .UrlBlockExceptions import *
class HostFile:

    DefaultRedirectUrl = "127.0.0.1"
    DefaultTopText = "# This host file was edited with DesktopUrlBlock.\n# For more information and help, go to the app's github page: https://github.com/11Firefox11/DesktopUrlBlock.\n"
    PlatformsPath = {"win":"c:\windows\system32\drivers\etc\hosts", "linux":"/etc/hosts", "darwin":"/etc/hosts"}

    def __init__(self):
        self.info = []

    def SetContent(self, o, settype="simple"):
        if self.CheckForPermission() and o != None and o != "":
            if settype=="simple":
                if type(o) == list:
                    finalcontent = ""
                    for part in o:
                        if part != "" and part != None:
                            finalcontent += str(part) + "\n"
                    o = finalcontent
                    with open(HostFilePath, "w") as file:
                        file.write(f"{HostFile.DefaultTopText}{o}")
            elif settype == "remove":
                content = self.HostFileContent
                file = open(HostFilePath, "w")
                final = []
                if type(o) != list:
                    o = [o]
                justints = [x for x in o if type(x) == int]
                for partindex in range(len(content)):
                    if content[partindex] in o:
                        o.remove(content[partindex])
                    elif partindex in justints:
                        justints.remove(partindex)
                    else:
                        final.append(str(content[partindex]))
                final = "".join(final)
                self.info = o + justints
                with open(HostFilePath, "w") as file:
                    file.write(f"{HostFile.DefaultTopText}{final}")
            elif settype == "add":
                self.HostFileContent
                file = open(HostFilePath, "a")
                if type(o) == list:
                    for part in o:
                        file.write(part + "\n")
                else:
                    file.write(o + "\n")
            return True

    @property
    def HostFileContent(self):
        if HostFile.CheckForPermission():
            text = open(HostFilePath, "r").readlines()
            if bool(text) == False:
                text = ""
            if len(text) >= 2 and "".join(text[:2]) == HostFile.DefaultTopText or "".join(text[:2]) + "\n" == HostFile.DefaultTopText:
                return text[2:]
            else:
                open(HostFilePath, "w").write(f"{HostFile.DefaultTopText}{text}")
                return text

    @staticmethod
    def CheckForPermission():
        try:
            open(HostFilePath, "a")
            return True
        except:
            raise PermissionNotGranted(HostFilePath)

    @staticmethod
    def MakeSyntax(urls : list):
        for urlindex in range(len(urls)):
            urls[urlindex] = str(urls[urlindex]).replace(" ", "%20")
        if len(urls) < 2:
            urls.append(HostFile.DefaultRedirectUrl)
        return f"{urls[0]} {urls[1]}"

HostFilePath = "".join([HostFile.PlatformsPath[pl] for pl in HostFile.PlatformsPath if sys.platform.startswith(pl)])