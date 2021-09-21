import sys
from UrlBlockExceptions import *
class HostFile:

    DefaultRedirectUrl = "127.0.0.1"
    DefaultTopText = "# This host file was edited with DesktopUrlBlock.\n# For more information and help, go to the app's github page: https://github.com/11Firefox11/DesktopUrlBlock."
    PlatformsPath = {"win":"c:\windows\system32\drivers\etc\hosts", "linux":"/etc/hosts", "darwin":"/etc/hosts"}

    @staticmethod
    def SetContent(content):
        if HostFile.CheckForPermission() and content != None and content != "":
            if type(content) == list:
                finalcontent = ""
                for part in content:
                    if part != "" and part != None:
                        finalcontent += str(part) + "\n"
                content = finalcontent
            with open(HostFilePath, "w+") as file:
                file.write(f"{HostFile.DefaultTopText}\n{content}")
            return True

    @staticmethod
    def Remove(o):
        pass

    @staticmethod
    def Add(o):
        pass

    @property
    def HostFileContent():
        if HostFile.CheckForPermission():
            return open(HostFilePath, "r+").readlines()

    @staticmethod
    def CheckForPermission():
        try:
            with open(HostFilePath, "w+") as file:
                pass
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

print(HostFile().SetContent(["xd",""]))