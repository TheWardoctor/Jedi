import xbmc,xbmcaddon,xbmcvfs,xbmcgui
import sys
which = sys.argv[1]

ADDON = xbmcaddon.Addon(id='script.jedi.guide')

if which == "commands":
    path = xbmc.translatePath('special://home/addons/script.jedi.guide/commands.txt')
elif which == "autoplaywith":
    path = xbmc.translatePath('special://home/addons/script.jedi.guide/resources/playwith/readme.txt')
f = xbmcvfs.File(path,"rb")
data = f.read()
dialog = xbmcgui.Dialog()
dialog.textviewer('Help', data)
