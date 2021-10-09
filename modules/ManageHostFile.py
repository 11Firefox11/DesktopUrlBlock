import sys, copy
from .UrlBlockExceptions import *
class HostFile:

    DefaultRedirectUrl = "127.0.0.1"
    DefaultTopText = "# This host file was edited with DesktopUrlBlock.\n# For more information and help, go to the app's github page: https://github.com/11Firefox11/DesktopUrlBlock.\n"
    PlatformsPath = {"win":"c:\windows\system32\drivers\etc\hosts", "linux":"/etc/hosts", "darwin":"/etc/hosts"}

    def __init__(self):
        self.info = []

    def SetContent(self, o, settype="simple"):
        if self.CheckForPermission() and o != None:
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
                copycontent = copy.deepcopy(content)
                if bool(content) == False:
                    raise IsEmpty(HostFilePath, "host file", "host file is empty, can't remove anything from it")
                file = open(HostFilePath, "w")
                final = []
                justints = o if type(o) == int else []
                for partindex in range(len(content)):
                    if partindex == justints:
                        justints == partindex
                    elif o == content[partindex].split(" ")[1][:-1] and o.isnumeric() == False:
                        copycontent.remove(content[partindex])
                    else:
                        final.append(str(content[partindex]))
                final = "".join(final)
                with open(HostFilePath, "w") as file:
                    file.write(f"{HostFile.DefaultTopText}{final}")
                if final == "".join(content):
                    return False
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
        if len(urls) >= 2:
            if urls[1] == None or urls[1] == "":
                urls[1] = HostFile.DefaultRedirectUrl
            for urlindex in range(len(urls)):
                urls[urlindex] = str(urls[urlindex]).replace(" ", "%20")
            return f"{urls[1]} {urls[0]}"
        else:
            return False

HostFilePath = "".join([HostFile.PlatformsPath[pl] for pl in HostFile.PlatformsPath if sys.platform.startswith(pl)])