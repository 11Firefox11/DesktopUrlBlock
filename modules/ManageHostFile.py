import sys, ctypes
from UrlBlockExceptions import *
class HostFile:

    DefaultRedirectUrl = "127.0.0.1"
    DefaultTopText = "# This host file was edited with DesktopUrlBlock.\n# For more information and help, go to the app's github page: https://github.com/11Firefox11/DesktopUrlBlock.\n"
    PlatformsPath = {"win":"c:\windows\system32\drivers\etc\hosts", "linux":"/etc/hosts", "darwin":"/etc/hosts"}

    def SetContent(self, content, settype=None):
        if self.CheckForPermission() and content != None and content != "":
            if type(content) == list:
                finalcontent = ""
                for part in content:
                    if part != "" and part != None:
                        finalcontent += str(part) + "\n"
                content = finalcontent
            if settype == "add":
                self.HostFileContent
            with open(HostFilePath, "w+") as file:
                file.write(f"{HostFile.DefaultTopText}{content}")
            return True

    @property
    def HostFileContent(self):
        if HostFile.CheckForPermission():
            text = open(HostFilePath, "r").readlines()
            if len(text) > 2 and "".join(text[:2]) == HostFile.DefaultTopText:
                return text[2:]
            else:
                print("".join(text[:2]), HostFile.DefaultTopText)
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
        return f"{urls[0]}\t{urls[1]}"

HostFilePath = "".join([HostFile.PlatformsPath[pl] for pl in HostFile.PlatformsPath if sys.platform.startswith(pl)])

HostFile().SetContent("xd")
print(HostFile().HostFileContent)