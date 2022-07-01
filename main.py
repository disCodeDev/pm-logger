import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@bot.command()
async def pmanity(ctx):
    embed = discord.Embed(description="**Playmanity** is a new generation gamimg platform for all of the users around the world. We provide everyone free games using ads. This is not anoying at all, because the ads only play when the game is starting, loading or you exit the game. We bring hundreds of players to our platform every day, why don't you join? \n ** ** \nJoin our discord server for more detailed information about our platform.\n> **https://discord.gg/AERk6WrzBS**", color=0x4c00ff)
    embed.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
    embed.set_footer(text="Playmanity Security - 2022®")#, timestamp=datetime.utcnow())
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('-help・Plaimanity.com'))
    print('Logged in!')

bot.run(os.environ['DISCORD_TOKEN'])