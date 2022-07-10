"""
Main function of logger. Start logger aswell as define commands and
load cogs
"""

# Import Discord Library
from discord.ext import commands, tasks
import discord
import asyncio
import aiohttp
import datetime
import warnings
import os
import json
import psutil
from datetime import datetime
import autopep8

# Import settings
from settings import bot_admin_ids, bot_host_id, command_prefix, token, version

# Import sys so we can send errors to stderr
import sys

# Base Bot
warnings.filterwarnings("ignore", category=DeprecationWarning)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=command_prefix, status=discord.Status.do_not_disturb, activity=discord.Game(name='Starting...'), intents=intents)
bot.remove_command('help')
bot.session = aiohttp.ClientSession()

@bot.event
async def on_ready():
    print(f"Logger version: {version}")
    print(f"{bot.user.name}: {bot.user.id}")
    print("--- Ready! ---")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='-help・Playmanity.com'))
    while True:
        guild = bot.get_guild(823565989865979976)

        mchannel = bot.get_channel(995631123549921320)
        await mchannel.edit(name=f'🎮・Members: {len(guild.members)}')
        await asyncio.sleep(180)

        bchannel = bot.get_channel(995635444161187850)
        await bchannel.edit(name=f'🎮・Boosters: {str(guild.premium_subscribers)}')
        await asyncio.sleep(180)



# COGS
@bot.command()
async def load(ctx, cog: str):
    """Load a cog back into the bot if the cog was unloaded. Can only
    be used by bot admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.load_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\U0001F44D')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")
@bot.command()
async def unload(ctx, cog: str):
    """Unload a cog. Useful if a cog is behaving badly. Can only be
    used by bot admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.unload_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\U0001F44D')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")
@bot.command()
async def reload(ctx, cog: str):
    """Re-evaluate the cog's code. Useful if working on the cog's code
    and you want to quickly test your changes. Can only be used by bot
    admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.reload_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\U0001F44D')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")
@bot.command()
async def shutdown(ctx):
    """Allows the bot host to shutdown the bot. Useful if the host
    doesn't have access to the console
    """
    if ctx.message.author.id == bot_host_id:
        print(f"Shutdown issued by: {ctx.message.author}({ctx.message.author.id})")
        await ctx.message.add_reaction('\U0001F44B')

        # Ensure that the bot has exited
        try:
            await bot.close()
        except Exception as error:
            print(error)
            sys.exit(1)
def restart_bot(): 
    os.execv(sys.executable, ['python'] + sys.argv)
DEVID = 969215020384792597
@bot.command(aliases=["rst", "forceR", "rl"])
async def restart(ctx):
    if ctx.message.author.id == DEVID:
        await ctx.send(f"<:reddot:944562679710904390> **Restart** issued by: {ctx.message.author} (`{ctx.message.author.id}`)")
        await ctx.message.add_reaction('<:check:972371839412232192>')
        restart_bot()
    else:
        await ctx.channel.send("You don't have permissions to use this command")


async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with bot.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False



@bot.command()
@commands.has_permissions(kick_members=True)
async def timeout(ctx: commands.Context, member: discord.Member, until: int):
    handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
    if handshake:
        return await ctx.send(f"<:timeend:943568323570962432> {member} has been successfully timed out for {until} minutes.")
        member.send(f"<:timeend:943568323570962432> You have been timed out in {ctx.guild.name} for {until} minutes.")
    await ctx.send("<:oops:964606229341151373> Something went wrong!")


@bot.command()
async def node(ctx):
    bedem = discord.Embed(title = 'System Resource Usage', description = 'See CPU and memory usage of the system.')
    bedem.add_field(name = 'CPU Usage', value = f'{psutil.cpu_percent()}%', inline = False)
    bedem.add_field(name = 'Memory Usage', value = f'{psutil.virtual_memory().percent}%', inline = False)
    bedem.add_field(name = 'Available Memory', value = f'{psutil.virtual_memory().available / 1048576} / {psutil.virtual_memory().total / 1048576}MB', inline = False)
    await ctx.send(embed = bedem)

'''
@tasks.loop(seconds = 10)
async def edit_embed():
    #channel = bot.get_channel(989857651250855936)
    #message = channel.fetch_message(992797020433682497)
    msg = bot.get_channel(989857651250855936).fetch_message(992797020433682497)
    gamesemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
    gamesemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
    gamesemb.set_footer(text="Playmanity Security - 2022®")
    gamesemb.add_field(name="<:pmdot2:992498402594127962> Playmanity Games", value="Down here you can see the list of games we currently have: \n<:pmdot2:992498402594127962> Arpsic \n<:pmdot2:992498402594127962> The Kostka \n<:pmdot2:992498402594127962 Dark web \n<:pmdot2:992498402594127962 Secret Game: Exclusively Playmanity's Game! \n** **\n> That's all we have for now, but don't worry, we add more games every week! \n> If you are a game developer or publisher and want to work with us, please reach any of the staff team members to get started! Remember, you get a few perks ;)", inline=False)
    await msg.edit(embed=gamesemb)
'''


@bot.event
async def on_member_join(member):
    guild = bot.get_guild(823565989865979976)
    channel = bot.get_channel(993191985512992839)
    mc = guild.member_count
    welcomeembed = discord.Embed(description=f"> Yoo! **{member.name}** joined **Playmanity Discord!** \n> Now we have **{mc}** members.", timestamp=datetime.utcnow(), color=0x2F3136)
    welcomeembed.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png")
    welcomeembed.set_thumbnail(url=member.avatar_url)
    welcomeembed.set_footer(text="Playmanity security - 2022®")
    await channel.send(embed=welcomeembed)
    await asyncio.sleep(60)
    role = discord.utils.get(member.guild.roles, id=823569170976473098)
    await member.add_roles(role)


@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(823565989865979976)
    channel = bot.get_channel(993191985512992839)
    mc = guild.member_count
    leftembed = discord.Embed(description=f"> Sad... **{member.name}** left **Playmanity Discord!** \n> Now we have **{mc}** members.", timestamp=datetime.utcnow(), color=0x2F3136)
    leftembed.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png")
    leftembed.set_footer(text="Playmanity security - 2022®")
    await channel.send(embed=leftembed)


bot.load_extension('cogs.Messages')
bot.load_extension('cogs.Reactions')
bot.load_extension('cogs.Commands')
bot.load_extension('cogs.Tickets')
bot.load_extension('cogs.Help')
bot.load_extension('cogs.Config')
bot.load_extension('cogs.Uptime')
bot.load_extension('cogs.PM')
bot.run(os.environ['DISCORD_TOKEN'])
