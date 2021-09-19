import sys

class HostFile:

    DefaultRedirectUrl = "127.0.0.1"
    DefaultTopText = "This host file was edited with DesktopUrlBlock.\nFor more information and help, go to the app's github page: https://github.com/11Firefox11/DesktopUrlBlock."
    PlatformsPath = {"win":"c:\windows\system32\drivers\etc\hosts", "linux":"/etc/hosts", "darwin":"/etc/hosts"}
    HostFilePath = None 
    
    def __init__(self):
        HostFile.HostFilePath = "".join([HostFile.PlatformsPath[pl] for pl in HostFile.PlatformsPath if sys.platform.startswith(pl)])

    @staticmethod
    def MakeSyntax(urls : list):
        for urlindex in range(len(urls)):
            urls[urlindex] = str(urls[urlindex]).replace(" ", "%20")
        if len(urls) < 2:
            urls.append(HostFile.DefaultRedirectUrl)
        return f"{urls[0]}\t{urls[1]}"

print(HostFile().HostFilePath)