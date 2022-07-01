import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in!')

client.run(os.environ['login'])