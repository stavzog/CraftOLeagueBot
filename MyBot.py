import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from random import *
import math

Client = discord.Client()
client = commands.Bot(command_prefix = ":")

@client.event
async def on_ready():
    print("Bot is running! GG")
    await client.change_presence(game=discord.Game(name=':help'))

@client.event
async def on_message(message):
    if message.content.upper().startswith(":OWNER"):
        userID = message.author.id
        server_owner = discord.utils.get()
        await client.send_message(message.channel, "<@%s> the Owner is MrRos" % (userID))
    if message.content.upper().startswith(":ANNOUNCE"):
        role = discord.utils.get(message.server.roles,name="Announcer")
        if role.id in [role.id for role in message.author.roles]:
            userID = message.author.id
            
            args = message.content.split(" ")
            channel = discord.utils.get(message.server.channels, name='announcements', type=discord.ChannelType.text)
            await client.send_message(channel, "%s" % (" ".join(args[1:])))
            UserMsg = " ".join(args[1:])
            embed=discord.Embed(title="Msg sent", description="Your message was successfully sent", color=0x06ce97)
            embed.set_author(name="CraftOLeague", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
            embed.add_field(name="Message:", value=UserMsg, inline=False)
            await client.send_message(message.channel, embed=embed)
            
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> you do not have permission to use this command :)" % (userID))
    if message.content.upper().startswith(":HELP"):
        embed=discord.Embed(title="Help", description="Display all the commands", color=0x06ce97)
        embed.set_author(name="CraftOLeague", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
        #embed.add_field(name=":owner", value="Displays the Owner of the server", inline=False)
        embed.add_field(name=":annouce [msg]", value="Announces [msg] in the announcements channel (Only for @Announcer role)", inline=False)
        embed.add_field(name=":cmembers", value="Counts all the members in the server", inline=False)
        embed.add_field(name=":setup", value="Bot Setup in order to work", inline=False)
        embed.add_field(name=":nick [nickname]", value="Set your nickname to [nickname]", inline=False)
        embed.add_field(name=":clear", value="Clears all the messages of the current channel", inline=False)
        embed.add_field(name=":binfo", value="Displays some bot info", inline=False)
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith(":NICK"):
        args = message.content.split(" ")
        await client.change_nickname(message.author, " ".join(args[1:]))
    if message.content.upper().startswith(":CMEMBERS"):
        memberCount = 0
        x = message.server.members
        for member in x:
            memberCount = memberCount + 1
        await client.send_message(message.author, "There are %s members in your server(I am counting the bots too)" % (memberCount))
    if message.content.upper().startswith(":BINFO"):
        embed=discord.Embed(title="Bot Info", description="Some information about the bot", color=0x7d7d7d)
        embed.set_author(name="CraftOLeague", url="https://discord.gg/gFuac2r", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
        embed.add_field(name="Creator:", value="The creator of the bot is <@398580757335113739>", inline=False)
        embed.add_field(name="Made for:", value="The bot was originally made for a discord server called Craft O' League", inline=False)
        embed.set_footer(text="Copyright Craft O' League")
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith(":clear"):
        tmp = await client.send_message(message.channel, 'Clearing messages')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    if message.content.upper().startswith(":SETUP"):
        embed=discord.Embed(title="Setting up", description="Bot setup", color=0x9e6701)
        embed.add_field(name="Step 1.", value="You must have an announcements txt channel", inline=False)
        embed.add_field(name="Step 2.", value="You must have an Announcer role (capitalization counts)", inline=True)
        embed.add_field(name="Step 3.", value="You must have a welcome channel", inline=True)
        embed.set_footer(text="None of the above can be turned off!")
        await client.send_message(message.channel, embed=embed)
    



@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.server.channels, name='welcome', type=discord.ChannelType.text)
    await client.change_nickname(member, "[Member]%s" % (member.name))
    randMessages = ["Welcome to our firepit <@%s>" % (member.id),"Hey <@%s>, doorbell broken!Yell Ding Dong" % (member.id),"If our dog doesn't like u, we probbably won't either <@%s>" % (member.id),"<@%s> Beware of da... Aaam...Just beware!" % (member.id),"Well, <@%s> there is free wifi and pizza inside!" % (member.id)]
    randNum = math.floor(randint(1, 5))
    await client.send_message(channel, randMessages[randNum])





client.run("NDA2NzYwMDIwNDUwMDgyODM2.DVG24w.gkYfCdaBYnSkRSvnEdZlqvqCIcY")
