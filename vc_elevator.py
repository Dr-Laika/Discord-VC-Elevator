import discord
from discord.ext import commands
import os
import time
from dotenv import load_dotenv

# create the bot
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)

# import tokens and keys
load_dotenv('TOKEN.env')
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

def get_building(cur_guild):
    '''
    compiles a list of all voice channels and filters out the channels that do not fit the naming scheme of building floors\n
    Naming scheme: ["DG", "n OG", "n-1 OG", ... , "EG", "1 UG", ... "m UG"]
    '''
    voice_channels = []
    building_levels = []
    for channel in cur_guild:
        if str(channel.type) == "voice":
            voice_channels.append(channel)
    for channel in voice_channels:
        if channel[2:3] == "DG" or channel[3:4] == "DG":
            building_levels.append(channel)
        elif channel[2:3] == "DG" or channel[3:4] == "DG":
            building_levels.append(channel)
        elif channel[0:1] == "EG":
            building_levels.append(channel)
        elif channel[2:3] == "UG" or channel[3:4] == "UG":
            building_levels.append(channel)
    return building_levels
    
@client.command
async def elevate(ctx, *user: discord.Member):
    cur_guild = discord.Guild()
    old_channel = user.get_channel()
    building = get_building(cur_guild)
    for level in building:
        await user.move_to(level)
        time.sleep(5)
    await user.move_to(old_channel)

client.run(TOKEN)
