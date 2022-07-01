import discord
from discord.ext import commands
from datetime import datetime
import os

client = commands.Bot(command_prefix='p', intents=discord.Intents.all())

@client.command()
async def pmanity(ctx):
    embed = discord.Embed(description="**Playmanity** is a new generation gamimg platform for all of the users around the world. We provide everyone free games using ads. This is not anoying at all, because the ads only play when the game is starting, loading or you exit the game. We bring hundreds of players to our platform every day, why don't you join? \n ** ** \nJoin our discord server for more detailed information about our platform.\n> **https://discord.gg/AERk6WrzBS**", color=0x4c00ff)
    embed.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
    embed.set_footer(text="Playmanity Security - 2022®", timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print('Logged in!')

client.run(os.environ['DISCORD_TOKEN'])