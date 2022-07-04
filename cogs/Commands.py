import discord
import aiohttp
import datetime
import warnings
import asyncio
from discord.ext import commands
from discord import User
from discord.ext.commands import Bot, guild_only
from datetime import datetime
BlackList = ["https://discord.gg/", "discord.gg"]
DeveloperID = 969215020384792597

class Commands(commands.Cog):
    """Commands cog"""
    def __init__(self, bot):
        self.bot = bot

# MOD: +Avatar, +Ban, Echo, +Kick, +Mute {main file}, Nick, +Nuke, Purge, Serverinfo, Slowmode, Softban, Timer, Unban, Unmute, Userinfo. 

    @commands.command(aliases=["av", "avtr", "pfp", "picture"])
    async def avatar(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        if member == None:
            member = ctx.author
        userAvatarUrl = member.avatar_url
        user = member.name
        ave = discord.Embed(timestamp=datetime.utcnow())
        ave.set_author(name=f"{user}'s avatar:")
        ave.set_image(url=userAvatarUrl)
        #await ctx.senf(f"{user}'s Avatar:")
        #await ctx.send(userAvatarUrl)
        await ctx.send(embed=ave, delete_after=15)


    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send("<:oops:964606229341151373> Please mention theperson you want to ban!", delete_after=15)
        await ctx.message.delete()
        await member.ban(reason=reason)
        await member.send(f"**<:kick:943475341526175745> You have been banned in `{ctx.guild}`!** \n<:kick:943475341526175745> **Reason:** *{reason}*")
        await ctx.send(f"<:corect1:943464328252764230> Member **{member.display_name}** has been Banned!", delete_after=15)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f'<:kick:943475341526175745> **{member.display_name}** has been kicked from the server! \n<:kick:943475341526175745> Reason: *{reason}*', delete_after=15)

# --> MUTE


    @commands.command(aliases=["chnick", "changenick"])
    async def nick(self, ctx, member: discord.Member, nick):
        if member == None:
            member = ctx.author
        await member.edit(nick=nick)
        await ctx.send(f"<:verified:943603376376147978> {member.name}'s Nickname was changed to **{nick}**!")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None: 
            channel = ctx.message.channel
        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Channel has been Nuked!")
            await nuke_channel.delete()
            await new_channel.send(f"<:corect1:943464328252764230> **{ctx.author}** had successfully Nuked this channel!", delete_after=5)
        else:
            await ctx.send(f"<:oops:964606229341151373> Channel named {channel.name} not found!")

    @commands.command(aliases=["cl", "clear", "p"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = None):
        await ctx.message.delete()
        if amount == None:
            await ctx.send("<:oops:964606229341151373> Please give amount of messages you want to purge!", delete_after=15)
        await ctx.channel.purge(limit=amount + 1)
        clearemb = discord.Embed(title=f"<:corect1:943464328252764230> Purge Successful!", description=f"<:trashcan:943464328412168212> **{amount}** messages were deleted!")
        clearemb.set_footer(text=f"Command performed by {ctx.author}!")
        await ctx.send(embed=clearemb, delete_after=15)


    @commands.command(aliases=["slowm", "sm"])
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.message.delete()
        await ctx.channel.edit(slowmode_delay=seconds)
        slowmode_embed = discord.Embed(title="<:corect1:943464328252764230> Channel Slowmode Changed", description=f"Slowmode to this channel has been set to **{seconds} seconds!**", colour=discord.Colour.green())
        await ctx.send(embed=slowmode_embed, delete_after=5)

    @commands.command(aliases=['sb'])
    @commands.has_permissions(kick_members=True)
    async def softban(self, ctx, member: discord.Member=None):
        await ctx.message.delete()
        if member == None:
            await ctx.send("<:oops:964606229341151373> Please mention member you want to SoftBan!", delete_after=15)
        inv = await ctx.channel.create_invite(max_uses=1)
        await member.send(f"<:kick:943475341526175745> You got softbanned from {ctx.author.guild}\n<:kick:943475341526175745> Join again with this link: {inv}")
        await ctx.guild.ban(member)
        await asyncio.sleep(0.1)
        await ctx.guild.unban(member)
        await ctx.send(f"<:kick:943475341526175745> **{member.name}** was softbanned by {ctx.author.mention}!", delete_after=15)

    @commands.command()
    async def timer(self, ctx, time):
        try:
            try:
                time = int(time)
            except:
                convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
                time = int(time[:-1]) * convertTimeList[time[-1]]
            if time > 172800:
                await ctx.send("<:oops:964606229341151373> Maximum Timer time is 2 days!")
                return
            if time <= 0:
                await ctx.send("<:oops:964606229341151373> Timer can't be shorter than 1 second")
                return
            if time >= 3600:
                message = await ctx.send(f"<:clock:943568320119070760> Time left: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
            elif time >= 60:
                message = await ctx.send(f"<:clock:943568320119070760> Time left: {time//60} minutes {time%60} seconds")
            elif time < 60:
                message = await ctx.send(f"<:clock:943568320119070760> Time left: {time} seconds")
            while True:
                try:
                    await asyncio.sleep(1)
                    time -= 1
                    if time >= 3600:
                        await message.edit(content=f"<:clock:943568320119070760> Time left: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                    elif time >= 60:
                        await message.edit(content=f"<:clock:943568320119070760> Time left: {time//60} minutes {time%60} seconds")
                    elif time < 60:
                        await message.edit(content=f"<:clock:943568320119070760> Time left: {time} seconds")
                    if time <= 0:
                        await message.edit(content="<:timeend:943568323570962432> Timer Ended!")
                        await ctx.author.send(f"{ctx.author.mention}, Your timer has ended!")
                        break
                except:
                    break
        except:
            await ctx.send(f"<:oops:964606229341151373> Something went wrong!")



    @commands.command(aliases=['unb'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int = None):
        await ctx.message.delete()
        if id == None:
            await ctx.send("<:oops:964606229341151373> Please give ID of the user you want to unban!", delete_after=15)
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"<:corect1:943464328252764230> Member {user} has been Unbanned!", delete_after=15)















    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author == DeveloperID:
            return
        for i in range(len(BlackList)):
            if BlackList[i] in message.content:
                for j in range(1):
                    await message.delete()
                    await message.author.send(f"**<:oops:964606229341151373> {message.author}**, don't use bad words in Playmanity Discord!")
'''   
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)
'''
def setup(bot):
    bot.add_cog(Commands(bot))
    print("Commands cog loaded")