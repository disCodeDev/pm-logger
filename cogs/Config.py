# Setting `Playing ` status
#await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

# DND - F04747
# Online - 43B581
# IDle - fAA61A


from discord.ext import commands
import discord
from datetime import datetime

class Config(commands.Cog):
    """Bot config cog"""
    def __init__(self, bot):
        self.bot = bot


    @commands.group(name='chs', invoke_without_command=True)
    async def chs(self, ctx):
        await ctx.message.delete()
        chse = discord.Embed(description="<:dotgreen:975052882699239456> `play1` - Playing + Online \n<:dotred:975052882971869244> `play2` - Playing + DND \n<:dotorange:975052882632114226> `play3` - Playing + Idle \n** **\n<:bdot:972581630780784720> `stream` - Streaming \n** **\n<:dotgreen:975052882699239456> `listen1` - Listening + Online \n<:dotred:975052882971869244> `listen2` - Listening + DND \n<:dotorange:975052882632114226> `listen3` - Listening + Idle \n** **\n<:dotgreen:975052882699239456> `watch1` - Watching + Online \n<:dotred:975052882971869244> `watch2` - Watching + DND \n<:dotorange:975052882632114226> `watch3` - Watching + Idle", timestamp=datetime.utcnow())
        chse.set_author(name="Config > Bot status", icon_url="https://cdn.discordapp.com/emojis/972427970914443295.webp?size=96&quality=lossless")
        chse.set_footer(text="Build V1.1")
        if ctx.author.id == 969215020384792597:
            await ctx.send(embed=chse)
        #if ctx.author.id == 610517365226209324:
        #    await ctx.send(embed=chse)
        else:
            await ctx.send(f"<:oops:964606229341151373> Sorry, only the bot developer can use this command!")


    @chs.command(aliases=["playing1"])
    async def play1(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=msg))
    @chs.command(aliases=["playing2"])
    async def play2(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=msg))
    @chs.command(aliases=["playing3"])
    async def play3(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=msg))


    @chs.command(aliases=["streaming"])
    async def stream(self, ctx, msg, link):
        await ctx.message.delete()
        await self.bot.change_presence(activity=discord.Streaming(name=msg, url=link))


    @chs.command(aliases=["listening1"])
    async def listen1(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=msg))
    @chs.command(aliases=["listening2"])
    async def listen2(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=msg))
    @chs.command(aliases=["listening3"])
    async def listen3(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=msg))


    @chs.command(aliases=["watching1"])
    async def watch1(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=msg))
    @chs.command(aliases=["watching2"])
    async def watch2(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=msg))
    @chs.command(aliases=["watching3"])
    async def watch3(self, ctx, msg):
        await ctx.message.delete()
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=msg))





def setup(bot):
    bot.add_cog(Config(bot))
    print("Config cog loaded")