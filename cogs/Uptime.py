import discord, datetime, time, calendar
from datetime import datetime
from discord.ext import commands

start_time = time.time()


class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = datetime.utcnow()
        difference = int(round(current_time - start_time))
        time = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=f"<t:{time}:F>")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("--- Current uptime: " + text)
"""
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = time
        gend = datetime.datetime.utcnow()
        utc = calendar.timegm(gend.utctimetuple())
        gendtime = utc + (amount * multiplier[unit])

        description=f":gw4: Hosted by: {ctx.author.mention}\n :gw4: React with 🎉  to enter!\n :gw4: Ends in: <t:{gendtime}:R>!

        embed.set_footer(text="Sponsored by altcointrain.com - Choo!!! Choo!!!")
"""



def setup(bot):
    bot.add_cog(Uptime(bot))
    print("Uptime cog loaded!")