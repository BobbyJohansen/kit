import cleverbot
import discord
import time
import image
import weather
import paxdate
import simplejson
import timetillpax

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

@client.event
def on_ready():
    print ('ready to go pew pew')


client.run()