import discord
import os

bot = commands.Bot(prefix, intents = intents)

@bot.event
async def on_ready():
    print('Logged in!')

bot.run(os.environ['login'])