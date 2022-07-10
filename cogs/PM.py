import discord
from discord.ext import commands
from datetime import datetime


class Playmanity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.has_permissions()
    async def dcideas(self, ctx):
        await ctx.message.delete()
        ideasemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
        ideasemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        ideasemb.set_footer(text="Playmanity Security - 2022®")
        ideasemb.add_field(name="<:pmdot2:992498402594127962> Playmanity Ideas", value="In this channel you can post your suggestions to our platform or discord server.\n**Template:** `-newidea \"idea title\" idea description` \n** **\n> **IMPORTANT NOTES:** \n1. Post your game suggestions to <#992308123735961660> channel! \n2. Don't forget to add `\"\"`when using multiple words in title!", inline=False)
        await ctx.send(embed=ideasemb)


    @commands.command()
    @commands.has_permissions()
    async def edit(self, ctx):
        channel = discord.utils.get(ctx.guild.text_channels, name="💡・ideas")
        #channel = self.bot.get_channel(992048478882627594) # the message's channel
        msg_id = 992882653571330118 # the message's id
        msg = await ctx.channel.fetch_message(msg_id)
        await msg.edit(embed=ideasemb)

    @commands.command()
    @commands.has_permissions()
    async def newidea(self, ctx, title, *, idea):
        await ctx.message.delete()
        channel = self.bot.get_channel(992048478882627594)
        newideaemb = discord.Embed(description=f"> {idea}", timestamp=datetime.utcnow(), color=0x2F3136)
        newideaemb.set_author(name=f"New Idea! ・ {title}", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        newideaemb.set_footer(text=f"Idea by: {ctx.author.name} ・ {ctx.author.id} \nPlaymanity Security - 2022®")
        await channel.send(embed=newideaemb)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name != "💡・ideas":
            return
        await message.add_reaction("<:up:993485860139958353>")
        await message.add_reaction("<:down:993485861624754286>")
        
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        upvote = "<:up:993485860139958353>"
        downvote = "<:down:993485861624754286>"
        up_needed = 2 # Number of upvotes needed
        down_needed = 15 # Number of downvotes needed
        idea_channel = self.bot.get_channel(993488586240430150) # Staff Team channel

        if reaction.message.channel.name != "💡・ideas":
            return

        if (reaction.emoji == upvote) and (reaction.count == up_needed):
            await idea_channel.send(f"This idea has reached {str(up_needed)} upvotes, and waiting to be reviewed by Staff Team!")
            await idea_channel.send(reaction.message.content)
            await message.author.send(f"Your idea has reached {str(up_needed)} upvotes, and waiting to be reviewed by Staff Team!")
            await message.author.send(reaction.message.content)
            await reaction.message.delete()
            #await bot.send_message(reaction.message.guild.get_member_named(admin), "A suggestion has reached " + str(up_needed) + " :arrow_up:!")
            #await bot.send_message(reaction.message.server.get_member_named(admin), reaction.message.content)

        #if (reaction.emoji == downvote) and (reaction.count == down_needed):
            #await bot.send_message(reaction.message.server.get_member_named(admin), "A suggestion has got " + str(down_needed) + " :arrow_down:!")
            #await bot.send_message(reaction.message.server.get_member_named(admin), reaction.message.content)
            #await reaction.message.delete()



    @commands.command()
    @commands.has_permissions()
    async def dcqna(self, ctx):
        qnaemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)




        await ctx.send("template command")


    @commands.command()
    @commands.has_permissions()
    async def dcinfo(self, ctx):
        await ctx.message.delete()
        infoemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
        infoemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        infoemb.set_footer(text="Playmanity Security - 2022®")
        infoemb.set_image(url="https://cdn.discordapp.com/attachments/991739957410537537/992759264571560036/Cover.png")
        infoemb.add_field(name="<:pmdot2:992498402594127962> Introduction:", value="**Playmanity** is a new generation gamimg platform for all of the users around the world. We provide everyone free games using ads. This is not anoying at all, because the ads only play when the game is starting, loading or you exit the game. We bring hundreds of players to our platform every day, why don't you join?", inline=False)
        infoemb.add_field(name="<:pmdot2:992498402594127962> Rules:", value="`01` ─ Treat everyone with respect. No harassment or threats, witch hunting, sexism, racism, or hate speech will be tolerated. \n`02` ─ Any type of discrimination, extreme swearing, and harassment is not allowed. \n`03` ─ No NSFW, drama, slander, or stirring (incl. fake news, unproven data). \n`04` ─ Spam is not welcome (this includes text walls). \n`05` ─ Use your common sense. \n`06` ─ Any type of advertisements are forbidden and can be reported via ticket. \n`07` ─ Any type of phishing is strictly not allowed and will result in an instant ban. \n`08` ─ Follow Discord's [Terms of Service](https://discord.com/terms) & [Community Guidelines](https://discord.com/guidelines)! \n` - ` Breaking any of these rules will insult to moderating action!", inline=False)
        infoemb.add_field(name="<:pmdot2:992498402594127962> Links:", value="[Kickstarter](https://www.kickstarter.com/projects/playmanity/playmanity?ref=8f8kr8&token=fdad64e2) ・ [Instagram](https://www.instagram.com/playmanity/) ・ [Twitter](https://twitter.com/playmanity) ・ [Telegram](https://t.me/playmanity) ・ [YouTube](https://www.youtube.com/channel/UCx6Lrn7heLP17FNc1eNqQZA) ・ [TikTok](https://www.tiktok.com/@playmanity)", inline=False)
        await ctx.send(embed=infoemb)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mntn(self, ctx):
        await ctx.message.delete()
        allowed_mentions = discord.AllowedMentions(everyone = True)
        await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions, delete_after=0.1)


    @commands.command()
    @commands.has_permissions()
    async def betatesters(self, ctx):
        await ctx.message.delete()
        betaemb = discord.Embed(description="<a:tada:993941547949248572> Finally, we want to introduce our BETA Launch! Thanks for being so active in our discord! Today we are making a giveaway where everyone are in the participants list for being with us on Discord. \n**On this occasion, we are giving away FREE 100 BETA Tester roles where you can try our app and platform!** And the best this is that you don't have to do anything! Just stay in this Discord Server and invite some of your friends for good luck :) \nWinners will be chosen on <t:1658912400:f>, so don't sleep, there isn't much time left! If we see a quick growth spurt, we might raise winners count, so invite your friends for better chances!\n** **\n<a:boost:993941539795505243> Introducing Exclusive Perks for Discord Server Boosters! Have a <@&993274019719692308> role? That's it! You are one of the first platform testers. Every server booster will get BETA Tester role and they don't be counted on the giveaway. So that means there will be more than 100 winners! Thanks for everyone who supports us on Discord! :heart:", timestamp=datetime.utcnow(), color=0x2F3136)
        betaemb.set_author(name="Playmanity BETA Launch!", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png")
        betaemb.set_footer(text="Playmanity Security - 2022®")
        await ctx.send(embed=betaemb)

    @commands.command()
    @commands.has_permissions()
    async def dcfaq(self, ctx):
        await ctx.message.delete()
        faqemb = discord.Embed(description="**Playmanity's FAQ - Frequently Asked Questions** \n<:pmdot1:992498404271857774> **Q.** *How do I apply to BETA?*\n<:pmdot2:992498402594127962> **A.** Boost the server or wait untill June 25 and have a chance to win one.\n ** **\n<:pmdot1:992498404271857774> **Q.** *Where can I download Playmanity App?*\n<:pmdot2:992498402594127962> **A.** We are only currently in Development, so there is no way to download the app.\n ** **\n<:pmdot1:992498404271857774> **Q.** *Where can I find staff / support team forms?*\n<:pmdot2:992498402594127962> **A.** Currently we have enough Staff / Support Team members. We will announce in <#823567823305310229> channel if we need new team members.\n ** **\n<:pmdot1:992498404271857774> **Q.** *Is this a cloud gaming platform?*\n<:pmdot2:992498402594127962> **A.** No, for now, we don't support cloud gaming, but later on, maybe.\n ** **\n<:pmdot1:992498404271857774> **Q.** *Can I play this game on other OS than Windows?*\n<:pmdot2:992498402594127962> **A.** Yepp! We support Windows, MacOS and Linux operating systems.\n ** **\n<:pmdot1:992498404271857774> **Q.** *What games will there be?*\n<:pmdot2:992498402594127962> **A.** You can find all of our available games in <#989857651250855936> channel.\n ** **\n<:pmdot1:992498404271857774> **Q.** *How can I help you to grow financially?*\n<:pmdot2:992498402594127962> **A.** We will launch on Kickstarter on August 27, so you can support [here](https://www.kickstarter.com/projects/playmanity/playmanity?ref=8f8kr8&token=fdad64e2). Register and click **\"Notify me\"** and check for updates in social medias.\n ** **\n<:2_:994131277995323482> **If you have any more questions, please ask in <#992308123735961660> channel!**", timestamp=datetime.utcnow(), color=0x2F3136)
        faqemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        faqemb.set_footer(text="Playmanity Security - 2022®")
        await ctx.send(embed=faqemb)

    @commands.command()
    @commands.has_role('・Support')
    async def betarole(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("Please specify a user you want to give the role!")
        else:
            role = discord.utils.get(ctx.guild.roles, name="BETA Tester")
            await user.add_roles(role)
            await ctx.send(f"**{ctx.author.name}** gave **BETA Tester** role to {user.mention}!")
    

    @commands.command()
    @commands.has_permissions()
    async def mc(self, ctx):
        allmc = {len(guild.members)}
        mc = len([m for m in ctx.guild.members if not m.bot])
        bots = len(allmc - mc)
        mcemb = discord.Embed(description=f"<:pmdot2:992498402594127962> All members: {allmc} \n<:pmdot2:992498402594127962> True members: {mc} \n<:pmdot2:992498402594127962> Bots: {bots}", timestamp=datetime.utcnow(), color=0x2F3136)
        mcemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        mcemb.set_footer(text="Playmanity Security - 2022®")
        await ctx.send(embed=mcemb)



'''
    @tasks.loop(seconds = 10, count=3)
    async def edit_embed(self):
        message = get_channel(989857651250855936).fetch_message(992797020433682497)
        #updated_embed = discord.Embed(title="Hi")
        gamesemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
        gamesemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        gamesemb.set_footer(text="Playmanity Security - 2022®")
        gamesemb.add_field(name="<:pmdot2:992498402594127962> Playmanity Games", value="Down here you can see the list of games we currently have: \n<:pmdot2:992498402594127962> Arpsic \n<:pmdot2:992498402594127962> The Kostka \n :pmdot2: Secret Game: Exclusively Playmanity's Game! \n** **\n> That's all we have for now, but don't worry, we add more games every week! \n> If you are a game developer or publisher and want to work with us, please reach any of the staff team members to get started! Remember, you get a few perks ;)", inline=False)
        message.edit(embed=gamesemb)

    @commands.command()
    @commands.has_permissions()
    async def dcgames(self, ctx):
        await ctx.message.delete()
        gamesemb = discord.Embed(timestamp=datetime.utcnow(), color=0x2F3136)
        gamesemb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        gamesemb.set_footer(text="Playmanity Security - 2022®")
        gamesemb.add_field(name="<:pmdot2:992498402594127962> Playmanity Games", value="Down here you can see the list of games we currently have: \n<:pmdot2:992498402594127962> Arpsic \n<:pmdot2:992498402594127962> The Kostka \n** **\n> That's all we have for now, but don't worry, we add more games every week! \n> If you are a game developer or publisher and want to work with us, please reach any of the staff team members to get started! Remember, you get a few perks ;)", inline=False)
        await ctx.send(embed=gamesemb)
'''











def setup(bot):
    bot.add_cog(Playmanity(bot))
    print("Playmanity Security is loaded!")