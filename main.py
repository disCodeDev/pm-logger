import discord
import os

client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in!')

bot.run(os.environ['login'])