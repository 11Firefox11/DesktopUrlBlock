import os, argparse, pathlib, sys, traceback
from modules.ManageHostFile import HostFile, HostFilePath
from modules.ManagePresetsFile import PresetsFile
from modules.UrlBlockExceptions import *

class Main:

    Version = "1.0.0"
    OutputTypes = {"info":"INFO: ", "input":"INPUT: ", "error": "ERROR: "}
    DefHelpInfoText = "For help in this curtain topic, visit:"
    DefEpilog = "For more information and help, go to the app's github page: https://github.com/11Firefox11/DesktopUrlBlock/."

    def __init__(self):
        self.Commands = {
                    "add":{
                        "help":"Add urls to the host file.", 
                        "desc":"Add urls to the host file, with giving an url and its redirect url.",
                        "version":"1.0",
                        "func":Main.add_url,
                        "args": {
                                "url":{"help":"Specify an url what will be redirected/blocked."},
                                "--redirect":{"help":"Specify an url where the url will be redirected to. If not specifed, default redirect url will be used."}
                            }
                        },
                    "remove":{
                        "help":"Remove urls from the host file.", 
                        "desc":"Remove urls from the host file, with giving the main url or an index.",
                        "version":"1.0",
                        "func":Main.remove_url,
                        "args": {
                                "url":{"help":"Specify an url what will be removed, or specify the index of the url you want to delete."}
                            }
                        }
                    }
        self.InitArgparse()

    def InitArgparse(self):
        parser = argparse.ArgumentParser(add_help=False, description=f"Desktop URL Block - {Main.Version}", epilog=Main.DefEpilog) 
        subparsers = parser.add_subparsers(help="List of available commands.")
        for command in self.Commands:
            commanddict = self.Commands[command]
            commandparse = subparsers.add_parser(command, help=commanddict["help"], add_help=False, description=commanddict["desc"])
            for arg in commanddict["args"]:
                argdict = commanddict["args"][arg]
                if "default" not in argdict:
                    argdict["default"] = None
                commandparse.add_argument(arg, help=argdict["help"], default=argdict["default"])
            commandparse.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help=f"Show help about this command ({command}).")
            commandparse.add_argument('--version','-v', action='version',version=f"{Main.OutputTypes['info']}Command '{command}' version: {self.Commands[command]['version']}", help="Shows commands's version number.")
            commandparse.set_defaults(func=commanddict['func'])
        parser.add_argument('--version','-v', action='version',version=f"Clever Template version: {Main.Version}", help="Shows app's version number.")
        parser.add_argument('--help','-h', action='help', default=argparse.SUPPRESS, help='Shows help about the app.')
        args = parser.parse_args()
        try:
            args.func(self, args)
        except Exception as e:
            if e.__class__.__name__ == "AttributeError":
                parser.print_help()
            else:
                self.Output("error", e)
                self.Output("info", Main.DefEpilog)

    def remove_url(self, args):
        try:
            args.url = int(args.url)
        except:
            pass
        HostFile().SetContent(args.url, "remove")
        self.Output("info", f"Successfully removed `{args.url}` from the host file. ({HostFilePath})")

    def add_url(self, args):
        urls = HostFile().MakeSyntax([args.redirect, args.url])
        if urls:
            HostFile().SetContent(urls, "add")
            self.Output("info", f"Successfully added `{urls}` to host file. ({HostFilePath})")

    @staticmethod
    def Output(outputtype, text, endprint="\n"):
        text = Main.OutputTypes[outputtype]+ str(text)
        if outputtype in Main.OutputTypes:
            print(text, end=endprint)

Main()