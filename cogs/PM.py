import discord
from discord.ext import commands
from datetime import datetime

class Playmanity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions()
    async def dcgames(self, ctx):
        gamesemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
        gamesemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        gamesemb.set_footer(text="Playmanity Security - 2022®")
        gamesemb.add_field(name="Playmanity Games", value="Down here you can see the list of games we currently have: \n<:pmdot2:992498402594127962> Arpsic \n<:pmdot2:992498402594127962> The Kostka \n** **\n> That's all we have for now, but don't worry, we add more games every week! \n> If you are a game developer or publisher and want to work with us, please reach any of the staff team members to get started! Remember, you get a few perks ;)", inline=False)
        await ctx.send(embed=gamesemb)

    @commands.command()
    @commands.has_permissions()
    async def dcideas(self, ctx):
        ideasemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)




        await ctx.send("template command")

    @commands.command()
    @commands.has_permissions()
    async def dcqna(self, ctx):
        qnaemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)




        await ctx.send("template command")


    @commands.command()
    @commands.has_permissions()
    async def dcinfo(self, ctx):
        infoemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
        infoemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        infoemb.set_footer(text="Playmanity Security - 2022®")
        infoemb.add_field(name="<:pmdot2:992498402594127962> Introduction:", value="**Playmanity** is a new generation gamimg platform for all of the users around the world. We provide everyone free games using ads. This is not anoying at all, because the ads only play when the game is starting, loading or you exit the game. We bring hundreds of players to our platform every day, why don't you join?", inline=False)
        infoemb.add_field(name="<:pmdot2:992498402594127962> Rules:", value="`01` ─ Treat everyone with respect. No harassment or threats, witch hunting, sexism, racism, or hate speech will be tolerated. \n`02` ─ Any type of discrimination, extreme swearing, and harassment is not allowed. \n`03` ─ No NSFW, drama, slander, or stirring (incl. fake news, unproven data). \n`04` ─ Spam is not welcome (this includes text walls). \n`05` ─ Use your common sense. \n`06` ─ Any type of advertisements are forbidden and can be reported via ticket. \n`07` ─ Any type of phishing is strictly not allowed and will result in an instant ban. \n`08` ─ Follow Discord's [Terms of Service](https://discord.com/terms) & [Community Guidelines](https://discord.com/guidelines)! \n` - ` Breaking any of these rules will insult to moderating action!", inline=False)
        infoemb.add_field(name="<:pmdot2:992498402594127962> Links:", value="[Kickstarter](https://www.kickstarter.com/projects/playmanity/playmanity?ref=8f8kr8&token=fdad64e2) ・ [Instagram](https://www.instagram.com/playmanity/) ・ [Twitter](https://twitter.com/playmanity) ・ [Telegram](https://t.me/playmanity) ・ [YouTube](https://www.youtube.com/channel/UCx6Lrn7heLP17FNc1eNqQZA) ・ [TikTok](https://www.tiktok.com/@playmanity)", inline=False)
        await ctx.send(embed=infoemb)


def setup(bot):
    bot.add_cog(Playmanity(bot))
    print("Playmanity Security is loaded!")