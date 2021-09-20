# Desktop URL block
## Introduction
This would be a simple python console based app. As the name says, it would be for blocking URL-s on Desktops.  
There is a host file on all type of os, Windows, Linux, MacOs.  
The host file is just simply a file, where you can define that what url should be redirected to what url, globally, on the pc/laptop or whatever device.  
So the user could define, what websites/urls should be blocked, and how.  
There would be presets in a json file, you could give presets a name, edit them, or you can just add some urls no matter to the presets.  
You could add timers, to what should be executed when.  
There would be a special web server, what would be an "extension" for the app, it could do some simple things, like by the redirecting url, count how many times the user tried to go on a curtain website and when, but for now, let's just leave that for a future plan.  
## Main classes
### Main 
ClassVariables: Version, DefEpilog, OutputTypes 
Methods: InitArgpharse, add, remove, preset(load, add, remove, reset, set), reset
StaticMethods: Output
### HostFile
ClassVariables: DefaultTopText, DefaultRedirectUrl
Methods: Add, Remove, SetContent
StaticMethods: MakeSyntax
Properties: CurrentContent, Path  
### ConfigFile
ClassVariables: Path
Methods: Load, Add, Remove, Reset, Set
### UrlBlockExceptions