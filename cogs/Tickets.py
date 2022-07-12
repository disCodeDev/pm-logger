from discord.ext import commands
import discord
import json
import asyncio
from datetime import datetime
import autopep8


class Tickets(commands.Cog):
    """Tickets cog"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ticket(self, ctx):
        # 1st part
        t1emb = discord.Embed(description="Once you click the emoji at the end of this message, you will create a new channel called Ticket. Ticket is like private channel when only you and support team. \n** **\n**<:checkmark:996456819574702080> NOTE!** Only create the Ticket if you want to get more info about **becoming a game developer**!", timestamp=datetime.utcnow(), color=0x2F3136)
        t1emb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        t1emb.set_footer(text="Playmanity Security - 2022®")

        t1msg = await ctx.send(embed=t1emb)
        await t1msg.add_reaction('<:pm1:992308768710873158>')
        #reaction = await t1msg.fetch_message(msg.id)

        def check(reaction, user):
            return str(reaction) == '<:pm1:992308768710873158>' and ctx.author == user

        await self.bot.wait_for("reaction_add", check=check)
        with open("data.json") as f:
            data = json.load(f)
        tnumber = int(data["tcounter"])
        tnumber += 1
        tchannel = await ctx.guild.create_text_channel("・ticket-{}".format(tnumber))
        await tchannel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

        for role_id in data["valid-roles"]:
            role = ctx.guild.get_role(role_id)
            await tchannel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        await tchannel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

        data["tchannel-ids"].append(tchannel.id)
        data["tcounter"] = int(tnumber)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        # 2nd part
        t2emb = discord.Embed(description="Thanks for making a ticket!", timestamp=datetime.utcnow(), color=0x2F3136)
        t2emb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
        t2emb.set_footer(text="Playmanity Security - 2022®")

        t2msg = await ctx.tchannel.send(f'<@823569100692783164>', embed=t2emb)
        await t2msg.add_reaction('<:xmark:996434171700461578>')

        with open('data.json') as f:
            data = json.load(f)

        if ctx.channel.id in data["tchannel-ids"]:
            channel_id = ctx.channel.id
            def check(reaction):
                return str(reaction) == '<:xmark:996434171700461578>' and ctx.author == user
            await self.bot.wait_for("reaction_add", check=check, timeout=60)
            try:    
                t3emb = discord.Embed(description="Are you sure you want to close this ticket? Add <:checkmark:996456819574702080> reaction to confirm!", color=0x2F3136)
                t3emb.set_author(name="Playmanity Security", url="https://playmanity.com", icon_url="https://media.discordapp.net/attachments/991739957410537537/992050893388271676/Logo_dark.png?width=409&height=409")
                t3emb.set_footer(text="Playmanity Security - 2022®")

                t3msg = await ctx.send(embed=t3emb)
                await t3msg.add_reaction('<:checkmark:996456819574702080>')

                def check(reaction):
                    return str(reaction) == '<:checkmark:996456819574702080>' and ctx.author == user

                await self.bot.wait_for("reaction_add", check=check, timeout=60)
                await ctx.send("<:checkmark:996456819574702080> This ticket automatically will close after **5 seconds!**")
                await asyncio.sleep(5)
                await ctx.channel.delete()

                index = data["tchannel-ids"].index(channel_id)
                del data["tchannel-ids"][index]
                with open('data.json', 'w') as f:
                    json.dump(data, f)
            except asyncio.TimeoutError:
                await ctx.send('An error occured!')
# ..........................................................................................................
#            except asyncio.TimeoutError:
#                em = discord.Embed(title="Auroris Tickets", description="You have run out of time to close this ticket. Please run the command again.", color=0x2F3136)
#                await ctx.send(embed=em)



    @commands.command()
    async def new(self, ctx, *, args = None):
        await ctx.message.delete()
        await self.bot.wait_until_ready()
        if args == None:
            message_content = "Please wait, <@938149705622356048> will be with you shortly!"
        else:
            message_content = "".join(args)
        with open("data.json") as f:
            data = json.load(f)
        ticket_number = int(data["ticket-counter"])
        ticket_number += 1
        ticket_channel = await ctx.guild.create_text_channel("・ticket-{}".format(ticket_number))#, category=category)
        await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
        for role_id in data["valid-roles"]:
            role = ctx.guild.get_role(role_id)
            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        em = discord.Embed(title="New ticket from {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "{}".format(message_content), color=0x00a8ff)
        await ticket_channel.send(embed=em)
        pinged_msg_content = ""
        non_mentionable_roles = []
        if data["pinged-roles"] != []:
            for role_id in data["pinged-roles"]:
                role = ctx.guild.get_role(role_id)
                pinged_msg_content += role.mention
                pinged_msg_content += " "
                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)
            await ticket_channel.send(pinged_msg_content)
            for role in non_mentionable_roles:
                await role.edit(mentionable=False)
        data["ticket-channel-ids"].append(ticket_channel.id)
        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)
        created_em = discord.Embed(title="Playmanity Tickets", description="Your ticket has been created at {}".format(ticket_channel.mention), color=0x00a8ff)
        await ctx.send(embed=created_em, delete_after=10)

    @commands.command()
    async def close(self, ctx):
        with open('data.json') as f:
            data = json.load(f)
        if ctx.channel.id in data["ticket-channel-ids"]:
            channel_id = ctx.channel.id
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "close"
            try:
                em = discord.Embed(title="Auroris Tickets", description="Are you sure you want to close this ticket? Reply with `close` if you are sure.", color=0x00a8ff)
                await ctx.send(embed=em)
                await self.bot.wait_for('message', check=check, timeout=60)
                await ctx.send("<:excl:972407750053212241> This ticket automatically will close after **5 seconds!**")
                await asyncio.sleep(5)
                await ctx.channel.delete()
                index = data["ticket-channel-ids"].index(channel_id)
                del data["ticket-channel-ids"][index]
                with open('data.json', 'w') as f:
                    json.dump(data, f)
            except asyncio.TimeoutError:
                em = discord.Embed(title="Auroris Tickets", description="You have run out of time to close this ticket. Please run the command again.", color=0x00a8ff)
                await ctx.send(embed=em)

    @commands.command()
    async def add(self, ctx, role_id=None):
        with open('data.json') as f:
            data = json.load(f)
        valid_user = False
        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except:
                pass
        if valid_user or ctx.author.guild_permissions.administrator:
            role_id = int(role_id)
            if role_id not in data["valid-roles"]:
                try:
                    role = ctx.guild.get_role(role_id)
                    with open("data.json") as f:
                        data = json.load(f)
                    data["valid-roles"].append(role_id)
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    em = discord.Embed(title="Auroris Tickets", description="You have successfully added `{}` to the list of roles with access to tickets.".format(role.name), color=0x00a8ff)
                    await ctx.send(embed=em)
                except:
                    em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
                    await ctx.send(embed=em)
            else:
                em = discord.Embed(title="Auroris Tickets", description="That role already has access to tickets!", color=0x00a8ff)
                await ctx.send(embed=em)
        else:
            em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    async def remove(self, ctx, role_id=None):
        with open('data.json') as f:
            data = json.load(f)
        valid_user = False
        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except:
                pass
        if valid_user or ctx.author.guild_permissions.administrator:
            try:
                role_id = int(role_id)
                role = ctx.guild.get_role(role_id)
                with open("data.json") as f:
                    data = json.load(f)
                valid_roles = data["valid-roles"]
                if role_id in valid_roles:
                    index = valid_roles.index(role_id)
                    del valid_roles[index]
                    data["valid-roles"] = valid_roles
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    em = discord.Embed(title="Auroris Tickets", description="You have successfully removed `{}` from the list of roles with access to tickets.".format(role.name), color=0x00a8ff)
                    await ctx.send(embed=em)
                else:
                    em = discord.Embed(title="Auroris Tickets", description="That role already doesn't have access to tickets!", color=0x00a8ff)
                    await ctx.send(embed=em)
            except:
                em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)
        else:
            em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    async def addpingrole(self, ctx, role_id=None):
        with open('data.json') as f:
            data = json.load(f)
        valid_user = False
        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except:
                pass
        if valid_user or ctx.author.guild_permissions.administrator:
            role_id = int(role_id)
            if role_id not in data["pinged-roles"]:
                try:
                    role = ctx.guild.get_role(role_id)
                    with open("data.json") as f:
                        data = json.load(f)
                    data["pinged-roles"].append(role_id)
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    em = discord.Embed(title="Auroris Tickets", description="You have successfully added `{}` to the list of roles that get pinged when new tickets are created!".format(role.name), color=0x00a8ff)
                    await ctx.send(embed=em)
                except:
                    em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
                    await ctx.send(embed=em)
            else:
                em = discord.Embed(title="Auroris Tickets", description="That role already receives pings when tickets are created.", color=0x00a8ff)
                await ctx.send(embed=em)
        else:
            em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    async def removepingrole(self, ctx, role_id=None):
        with open('data.json') as f:
            data = json.load(f)
        valid_user = False
        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except:
                pass
        if valid_user or ctx.author.guild_permissions.administrator:
            try:
                role_id = int(role_id)
                role = ctx.guild.get_role(role_id)
                with open("data.json") as f:
                    data = json.load(f)
                pinged_roles = data["pinged-roles"]
                if role_id in pinged_roles:
                    index = pinged_roles.index(role_id)
                    del pinged_roles[index]
                    data["pinged-roles"] = pinged_roles
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    em = discord.Embed(title="Auroris Tickets", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)
                    await ctx.send(embed=em)
                else:
                    em = discord.Embed(title="Auroris Tickets", description="That role already isn't getting pinged when new tickets are created!", color=0x00a8ff)
                    await ctx.send(embed=em)
            except:
                em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)
        else:
            em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
            await ctx.send(embed=em)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addadmin(self, ctx, role_id=None):
        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)
            with open("data.json") as f:
                data = json.load(f)
            data["verified-roles"].append(role_id)
            with open('data.json', 'w') as f:
                json.dump(data, f)
            em = discord.Embed(title="Auroris Tickets", description="You have successfully added `{}` to the list of roles that can run admin-level commands!".format(role.name), color=0x00a8ff)
            await ctx.send(embed=em)
        except:
            em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeadmin(self, ctx, role_id=None):
        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)
            with open("data.json") as f:
                data = json.load(f)
            admin_roles = data["verified-roles"]
            if role_id in admin_roles:
                index = admin_roles.index(role_id)
                del admin_roles[index]
                data["verified-roles"] = admin_roles
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                em = discord.Embed(title="Auroris Tickets", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)
                await ctx.send(embed=em)
            else:
                em = discord.Embed(title="Auroris Tickets", description="That role isn't getting pinged when new tickets are created!", color=0x00a8ff)
                await ctx.send(embed=em)
        except:
            em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Tickets(bot))
    print("Tickets cog loaded")


"""
    @commands.command()
    async def thelp(self, ctx):
        with open("data.json") as f:
            data = json.load(f)
        valid_user = False
        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except:
                pass
        if ctx.author.guild_permissions.administrator or valid_user:
            em = discord.Embed(color=0x00a8ff, timestamp=datetime.utcnow())
            em.set_author(name="PaperBots - Tickets System", url="https://dsc.gg/pbots", icon_url=ctx.guild.icon_url)
            em.add_field(name="`.new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
            em.add_field(name="`.close`", value="Use this to close a ticket. This command only works in ticket channels.")
            em.add_field(name="`.addaccess <role_id>`", value="This can be used to give a specific role access to all tickets. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.delaccess <role_id>`", value="This can be used to remove a specific role's access to all tickets. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.addpingedrole <role_id>`", value="This command adds a role to the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.delpingedrole <role_id>`", value="This command removes a role from the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
            em.add_field(name="`.addadminrole <role_id>`", value="This command gives all users with a specific role access to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
            em.add_field(name="`.deladminrole <role_id>`", value="This command removes access for all users with the specified role to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
            em.set_footer(text="PBD • V1.1")
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title = "Auroris Tickets Help", description ="", color = 0x00a8ff)
            em.add_field(name="`.new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
            em.add_field(name="`.close`", value="Use this to close a ticket. This command only works in ticket channels.")
            em.set_footer(text="Auroris Development")
            await ctx.send(embed=em)
"""