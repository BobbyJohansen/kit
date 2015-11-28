import cleverbot
import discord
import simplejson
from pprint import pprint


# plugins
import image
import weather
import paxdate
import timetillpax
import reddit

def loadConfig():
    print ('loading config')
    config = {}
    with open('kitt.cfg', 'r') as f:
        config = simplejson.load(f)
        f.close()
    return config

config = loadConfig()
kit = cleverbot.Cleverbot()
client = discord.Client()
client.login(config['email'],config['password'])

if client.is_logged_in:
    print ('Logged into discord woo!')

def cleverResponse(message):
    response = kit.ask(message.content[5:])
    client.send_message(message.channel, response, False, False)
    
def img(content):
    return image.image(content, True)
    
    
def wthr(content):
    return weather.weather(content)

def pdate():
    return paxdate.paxdate()
    
def timeleft():
    return timetillpax.timetillpax()
    
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")
  
  
def allowPerm(channel, target, perm):
    client.set_channel_permissions(channel, target, discord.Permissions(), perm)
  
def denyPerm(channel, target, perm):
    client.set_channel_permissions(channel, target, perm, discord.Permissions())
  
    
    
# !reddit channelName
# !reddit rand unsafe
def getFromReddit(content):
    if content.startswith('rand'):
        unsafe = str2bool(content[5:])
        print (unsafe)
        return reddit.getRandomSubmissionFromAll(unsafe)
    else:
        try:
            return reddit.getRandSubmissionFromSub(content)
        except:
            print('Failed to get From reddit may not be a valid subreddit')

@client.event
def on_message(message):
    global config
    #match = re.findall(r"kitt image (.*)", message.content)
    print ('EVENT: ')
    print (message)
    print (message.content)
    if message.content.startswith(config['name']):
        cleverResponse(message)
    elif message.content.startswith('!image'):
        client.send_message(message.channel,img(message.content[7:]))
    elif message.content.startswith('!weather'):
        client.send_message(message.channel,wthr(message.content[9:]))
    elif message.content.startswith('!paxDate'):
        client.send_message(message.channel, pdate(), False, False)
    elif message.content.startswith('!timeTillPax'):
        client.send_message(message.channel, timeleft(), False, False)
    elif message.content.startswith('!reddit'):
        response = getFromReddit(message.content[8:])
        member = discord.utils.find(lambda m: m.name == 'Pax Bot', message.channel.server.members)
        print member
        perm = discord.Permissions()
        perm.can_embed_links = False
        denyPerm(message.channel, member, perm )
        client.send_message(message.channel,'Title: ' + response['title'] + 'Link: ' + response['link'])
        perm.can_embed_links = True
        allowPerm(message.channel, member, perm)


@client.event
def on_ready():
    print ('ready to go pew pew')


client.run()