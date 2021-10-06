<h1 align="center" id="Desktop URL Block">Desktop URL Block</h1>

<h4 align="center">Console app for "blocking" urls/hostnames/websites on desktop.</h4>
<p align="center"><img src="./assets/icon_dub.png" height="175"></p>

- [Introduction](#introduction)
- [Install](#install)
- [App usage](#app-usage)
  - [Commands](#commands)
    - [`add`](#add)
    - [`remove`](#remove)
## Introduction
Desktop URL Block is a console application, for blocking (redirecting) urls easily. Almost all desktop operating systems have a file called `hosts`. It is basically a plain text file, that maps hostnames to IP addresses. This is a system file, so for the full use of the app, **please give the app admin privileges**, or it will not work properly.
Desktop URL BLock uses that file, to redirect hostnames, to the localhost ip adress. So by that logic, the system will try to access the localhost ip adress when trying to load in that hostname/url/website, but there is no content on the localhost's ip, so by that it basically "blocks" the url.  
Dektop URL Block supports presets, what are basically list of urls, what can be named, loaded, edited. Presets work easy, for example you can add a preset by giving it a name, then input some urls in it, what to be blocked.

## Install
Download the code or the `DesktopUrlBlock.exe` file from a release. Github - [Dekstop URL Block Releases](https://github.com/11Firefox11/DesktopUrlBlock/releases)

## App usage
Open a terminal window on your device, and run Desktop URL Block, it is very important, to **run URL BLock Desktop with admin privileges**.  
If you simply run Desktop URL Block, it will give a help description about the app and its commands, arguments. You can interact with Desktop URL Block by commands.  
### Commands
Desktop URL Block uses simple syntaxes for commands. A command usually have arguments. There are positional arguments that must be in the command, and there are arguments which are optional, it means that it is not a must to be in the command. There are some default optional arguments.
#### `add`
With this command, the user can add new urls to block, by giving the url what will be redirected. The redirect ip adress (where the url will be redirected to) can be determined too, but it is not a must (then the default ip will be used). 
- #### Arguments:
`url`: This is a positional argument, it should point to an url, what will be added to the list of the blocked urls.  
`--redirect REDIRECT`: This is an optional argument, `REDIRECT` refers to be replaced with a redirect ip address, this will be the custom ip adress where the url will be redirected to. If it is not determined, default ip adress will be used: `127.0.0.1` (localhost).
- #### Command usage
```console
add [--redirect REDIRECT] url
```
#### `remove`
With this command, the user can remove urls what are currently on the blocking list. The user have to give the url, what to be removed.  
- #### Arguments:
`url`: This is a positional argument, it should point to an url or an index, what will be removed from the list of the blocked urls.
- #### Command usage
```console
remove url
```
