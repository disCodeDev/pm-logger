import discord
from discord.ext import commands

class Playmanity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def dcinfo(self, ctx):
        await ctx.send("template command")

    @commands.command()
    @commands.has_permissions()
    async def dcgames(self, ctx):
        await ctx.send("template command")

    @commands.command()
    @commands.has_permissions()
    async def dcideas(self, ctx):
        await ctx.send("template command")

    @commands.command()
    @commands.has_permissions()
    async def dcqna(self, ctx):
        await ctx.send("template command")


    @commands.command()
    @commands.has_permissions()
    async def dcinfo(self, ctx):
        embed = discord.Embed(description="**Playmanity** is a new generation gamimg platform for all of the users around the world. We provide everyone free games using ads. This is not anoying at all, because the ads only play when the game is starting, loading or you exit the game. We bring hundreds of players to our platform every day, why don't you join? \n ** ** \nJoin our discord server for more detailed information about our platform.\n> **https://discord.gg/AERk6WrzBS**", color=0x4c00ff)
        embed.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        embed.set_footer(text="Playmanity Security - 2022®")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Playmanity(bot))
    print("Playmanity Security is loaded!")