import discord
import os
from dotenv import load_dotenv


# create the bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# import tokens and keys
load_dotenv('TOKEN.env')
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)
