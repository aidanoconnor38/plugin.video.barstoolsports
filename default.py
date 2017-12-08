###########################################################################################################
#Import Modules and or Scripts
import sys
import plugintools
import xbmcaddon
from addon.common.addon import Addon
###########################################################################################################

###########################################################################################################
#Please change the addonID to match your folder / addon name exactly.
addonID = 'plugin.video.barstoolsports'
###########################################################################################################
#Feel free to change the color name in cr or cr1, do not edit cr2!
cr     = '[COLOR red][B]'
cr1    = '[COLOR snow][B]'
cr2    = '[/B][/COLOR]'
###########################################################################################################

###########################################################################################################
#Please do not edit these variables
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
###########################################################################################################

###########################################################################################################
#Channels and or Users Information from YouTube goes here
#Example:
#a1 = "The name of the channel or user goes here"
#a2 = "The channel or user /id goes here"
#a3 = 'The image icon url for the channel or user goes here'
#You can have as many channels / users as you wish, just be sure that you have a matching pair. For every
#letter number e1,e2,e3 you will also need to have (e1,e2,e3), 
###########################################################################################################
a1     = cr+"Barstool Sports"+cr2
a2     = "channel/UCifWD4FBa4eaKK7HLF0PlTA"
#a3     = 'http://vampinc.com/tksapps/icon.png'
a3     =  'http://www.barstoolsports.com/wp-content/uploads/2016/07/19/f1232624475d3dc1.png'
# ###########################################################################################################
# b1     = cr1+""+cr2
# b2     = ""
# b3     = ''
# ###########################################################################################################
# c1     = cr+""+cr2
# c2     = ""
# c3     = ''
# ###########################################################################################################
# d1     = cr1+""+cr2
# d2     = ""
# d3     = ''
###########################################################################################################
channellist=[ (a1, a2, a3)#,
#               (b1, b2, b3),
              # (c1, c2, c3),
              # (d1, d2, d3),
            ]
###########################################################################################################

###########################################################################################################
#Please do not edit this code
def run():
    plugintools.log("youtubeAddon.run")
    params = plugintools.get_params()
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()
###########################################################################################################

###########################################################################################################
#Please do not edit this code
def main_list(params):
    plugintools.log("youtubeAddon.main_list "+repr(params))
for name, id, icon in channellist:
    plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )
run()
###########################################################################################################