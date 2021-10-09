import argparse, traceback
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
                                "--redirect":{"help":f"Specify an ip adress where the url will be redirected to. If not specifed, default redirect ip adress will be used. ({HostFile.DefaultRedirectUrl})"}
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
                    },
                    "preset":{
                        "help":"Manage presets.",
                        "desc":"Manage presets saved in the main presets file. By giving a name, by default you can load in a preset. You can change managing types, for not just to add preset but do add, remove, set (content) presets.",
                        "version":"1.0",
                        "func":Main.preset,
                        "args":{
                            "name":{"help":"Specify a preset name what will be managed."},
                            "--type":{"help":"Specify the manage type. Default value is load. It can be: load, add, remove, set.", "default":"load"}
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
            if e.__class__.__name__ == "AttributeError" and "Namespace" in str(e):
                parser.print_help()
            else:
                self.Output("error", e)
                self.Output("info", Main.DefEpilog)

    def preset(self, args):
        addcontent = {}
        if args.type == "add" or args.type == "set":
            if args.type == "add":
                self.Output("info", f"Adding urls to preset: {args.name}")
            else:
                self.Output("info", f"Adding urls to preset: {args.name}")
            self.Output("info", "Please input the URL(s) what needs to be redirected/blocked, and their redirect ip adresses, if don't want to specify the redirect adress, then leave it blink.")
            self.Output("info", "To stop the inserting phrase, type `!q`.")
            defprints = ["URL", "REDIRECT (leave empty if want to use default)"]
            while True:
                print()
                content = []
                for prnt in defprints:
                    self.Output("input", f"{prnt}:", " ")
                    try:
                        data = input()
                    except KeyboardInterrupt:
                        break
                    if data == "!q":
                        break
                    else:
                        content.append(data)
                if len(content) >= 2:
                    content = HostFile.MakeSyntax(content).split(" ")
                    addcontent[content[1]] = content[0]
                else:
                    break
            PresetsFile().Manage(name=args.name, typem=args.type, value=addcontent)
        elif args.type == "load":
            self.Output("info", f"Loading in preset, checking for preset named: {args.name}...")
            content = PresetsFile().Manage(name=args.name, typem=args.type)
            self.Output("info", f"Successfully found the preset. Preset data: {content}.")
            HostFile().SetContent("")
            for c in content:
                self.Output("info", f"Adding `{c} {content}` to the host file...")
                HostFile().SetContent(HostFile().MakeSyntax([c, content[c]]), settype="add")
                self.Output("info", "Done.")
            addcontent = content
        elif args.type == "remove":
            self.Output("info", f"Removing preset by name: {args.name}")
            PresetsFile().Manage(args.name, typem="remove")
            addcontent = "Successful."
        else:
            self.Output("error", f"Preset manage type: `{args.type}`, does not exists!")
            exit()
        self.Output("info", f"Successfully executed: `{args.type}` to preset: `{args.name}`, with values: `{addcontent}`")

    def remove_url(self, args):
        try:
            args.url = int(args.url)
        except:
            pass
        HostFile().SetContent(args.url, "remove")
        self.Output("info", f"Successfully removed `{args.url}` from the host file. ({HostFilePath})")

    def add_url(self, args):
        urls = HostFile().MakeSyntax([args.url, args.redirect])
        if urls:
            HostFile().SetContent(urls, "add")
            self.Output("info", f"Successfully added `{urls}` to host file. ({HostFilePath})")

    @staticmethod
    def Output(outputtype, text, endprint="\n"):
        text = Main.OutputTypes[outputtype]+ str(text)
        if outputtype in Main.OutputTypes:
            print(text, end=endprint)

if __name__ == "__main__":
    Main()