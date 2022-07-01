from discord.ext import commands
import discord
import time
from datetime import datetime

class Help(commands.Cog):
    """Help cog"""
    def __init__(self, bot):
        self.bot = bot


    @commands.group(name='help', invoke_without_command=True, aliases=['?'])
    async def help(self, ctx):
        await ctx.message.delete()
        helpe = discord.Embed(description='<:Discord_Certified_Moderator:938765553227681822> **Commands Categories:** \n<:mod:972427971069640724> Moderation - `,help moderation` \n<:excl:972430928267845692> Logging - `,help logging` \n<:tickets:972427971216408606> Tickets - `,help tickets` \n<:dev:972427970914443295> Config - `,help config`', timestamp=datetime.utcnow())
        helpe.set_author(name="PaperBots - System Administrator!", url="https://dsc.gg/pbots/", icon_url=ctx.guild.icon_url)
        helpe.set_footer(text="Build V1.1")
        await ctx.send(embed=helpe)

# MOD: Ban, Kick, Mute, Purge, Slowmode, Softban, Timer, Unban, Unmute. 
    @help.command(aliases=['mod'])
    async def moderation(self, ctx):
        await ctx.message.delete()
        mode = discord.Embed(description="<:mod:972427971069640724> Commands: \n<:bdot:972581630780784720> `,ban <member> <reason>` - Bans member from the server. \n<:bdot:972581630780784720> `,kick <member> <reason>` - Kicks member from the server. \n<:bdot:972581630780784720> `,mute <member> <time> <reason>` - Mutes the server member. \n<:bdot:972581630780784720> `,nuke [channel]` - Nukes the given channel. \n<:bdot:972581630780784720> `,purge <count>` - Deletes given messages count. \n<:bdot:972581630780784720> `,slowmode <time>` - Sets a slowmode to a channel. \n<:bdot:972581630780784720> `,softban <member> <reason>` - Bans the member and instantly unbans them. \n<:bdot:972581630780784720> `,timer <time>` - Counts down given time. \n<:bdot:972581630780784720> `,unban <id>` - Unbans member from the server. *(Required ID!)* \n<:bdot:972581630780784720> `,unmute <member>` - Unmutes server member. \n** ** \n<:excl:972407750053212241> **`<>` - Optional!** \n<:excl:972407750053212241> **`[]` - Required!** \n** ** \n<:verified:943603376376147978> **All of these commands can only be executed by `SUPPORT TEAM` members!**", timestamp=datetime.utcnow())
        mode.set_author(name="System Administrator - Moderation!", url="https://dsc.gg/pbots/", icon_url=ctx.guild.icon_url)
        mode.set_footer(text="Build V1.1")
        await ctx.send(embed=mode)

    @help.command(aliases=['log'])
    async def logging(self, ctx):
        logge = discord.Embed(title=",help mod")
        await ctx.send(embed = logge)

        
    @help.command(aliases=["t", "ticket"])
    async def tickets(self, ctx):
        if ctx.author.guild_permissions.administrator:
            em = discord.Embed(timestamp=datetime.utcnow())
            em.set_author(name="PaperBots - Tickets System", url="https://dsc.gg/pbots", icon_url=ctx.guild.icon_url)
            em.add_field(name="`.new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
            em.add_field(name="`.close`", value="Use this to close a ticket. This command only works in ticket channels.")
            em.add_field(name="`.add <role_id>`", value="This can be used to give a specific role access to all tickets. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.remove <role_id>`", value="This can be used to remove a specific role's access to all tickets. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.addpingerole <role_id>`", value="This command adds a role to the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.removepingerole <role_id>`", value="This command removes a role from the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.addadmin <role_id>`", value="This command gives all users with a specific role access to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
            em.add_field(name="`.deladmin <role_id>`", value="This command removes access for all users with the specified role to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
            em.set_footer(text="PBD • V1.1")
            await ctx.send(embed=em)
        else:
            em = discord.Embed(timestamp=datetime.utcnow())
            em.set_author(name="PaperBots - Tickets System", url="https://dsc.gg/pbots", icon_url=ctx.guild.icon_url)
            em.add_field(name="`.new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
            em.add_field(name="`.close`", value="Use this to close a ticket. This command only works in ticket channels.")
            em.set_footer(text="Auroris Development")
            await ctx.send(embed=em)






    @help.command(aliases=['con'])
    async def config(self, ctx):
        confe = discord.Embed(title=",help mod")
        await ctx.send(embed = confe)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Help cog loaded")










"""
    @commands.command()
    async def status(self, ctx):
        state = discord.Embed(description=f'+ {self.bot.users.cache.size}')
        await ctx.send(embed = state)

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        try:
            await self.bot.say(embed=embed)
        except discord.HTTPException:
            await self.bot.say("Current uptime: " + text)
"""