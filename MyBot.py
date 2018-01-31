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
    await client.change_presence(game=discord.Game(name='with :help'))

@client.event
async def on_message(message):
    if message.content.upper().startswith(":OWNER"):
        userID = message.author.id
        server_owner = message.server.owner
        await client.send_message(message.channel, "<@%s> the owner of this current server is <@%s> !" % (userID, server_owner.id))
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
        await client.send_message(message.channel,"``` \n Help \n ------------------- \n :announce [msg] = Announces [msg] to the announcements(must have) channel \n \n :owner = Returns the owner of the current server \n \n :cmembers = Counts all the mebers of the server (including bots) \n \n :sentup = Returns bot setup needed to work \n \n :nick [nickname] = Sets your nickname to [nickname] \n \n :clear = Clears all the messages of the channel \n \n :binfo = Displays some bot info \n \n :rnum [how many] = Returns [how many] random numbers \n \n :code [msg] = Converts [msg] to an embed \n \n :msg [channel] [msg] = Sends [msg] to [channel] \n \n :invitelink = Gives an invite link to invite the bot \n ```")
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
    if message.content.upper().startswith(":RTGEN"):
        global counter
        global players
        global team
        global player
        team = []                             
        counter = 1                             
        args = message.content.split(" ")
        players = " ".join(args[1:])
        players = players.split(",")
        for player in players:
            player = math.floor(randint(0,len(players)-1))
            if players[player] != "Replaced":
                team.append(players[player])
                if len(team) >= len(players)/4:
                    await client.send_message(message.channel, "Team %s is: %s" % (counter, " ".join(players)))
                    team = []
                    players[player] = "Replaced"               
    
    if message.content.upper().startswith(":INVITELINK"):
        await client.send_message(message.channel, "Link: \n https://discordapp.com/oauth2/authorize?client_id=406760020450082836&scope=bot&permissions=2146958591")
        
    if message.content.upper().startswith(":MSG"):
        role = discord.utils.get(message.server.roles,name="Announcer")
        if role.id in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            arg1 = args[1]
            channel = discord.utils.get(message.server.channels, name=arg1, type=discord.ChannelType.text)
            arg2 = " ".join(args[2:])
            await client.send_message(channel, "%s" % (arg2))
            embed=discord.Embed(title="Msg sent", description="Your message was successfully sent", color=0x06ce97)
            embed.set_author(name="CraftOLeague", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
            embed.add_field(name="Message:", value=arg2, inline=False)
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(message.channel, "<@%s> You don't have permission to use this command!" % (message.author.id))
    if message.content.upper().startswith(":RNUM"):
        global randnums
        args = message.content.split(" ")
        args = " ".join(args[1:])
        randnums = []
        count = int(float(args))
        for x in range(0, count):
            num = math.floor(randint(1,9))
            randnums.append(num)
        randnums = str(randnums)
        await client.send_message(message.channel, "``` \n Random Numbers: %s \n ```" % (" ".join(randnums[0])))
    if message.content.upper().startswith(":CODE"):
        args = message.content.split(" ")
        embed=discord.Embed(description="%s" % (" ".join(args[1:])), color=0x008080)
        embed.set_author(name=message.author.name,icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
        



@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.server.channels, name='welcome', type=discord.ChannelType.text)
    await client.change_nickname(member, "[Member]%s" % (member.name))
    randMessages = ["Welcome to our server <@%s>!" % (member.id),"Welcome to our firepit <@%s>" % (member.id),"Hey <@%s>, doorbell broken!Yell Ding Dong" % (member.id),"If our dog doesn't like u, we probbably won't either <@%s>" % (member.id),"<@%s> Beware of da... Aaam...Just beware!" % (member.id),"Well, <@%s> there is free wifi and pizza inside!" % (member.id),"Looks like the God of Thunder, <@%s>, might stay for a dinner" % (member.id),"Hallo <@%s>, please ring doorbell and run, the dog needs exercise!" % (member.id),"Welcome <@%s>, to our neck of da woods" % (member.id),"<@%s> Smile, the paparatsi are coming" % (member.id), "If you forgot to bring popcorn <@%s>, I 'll call the dog" % (member.id),"Come and see our campfire <@%s>, where friends and marshmellows become **Toasted**" % (member.id),"I’ve been waiting in the corner, with honor, for your coming, with your daughter! Welcome <@%s>" % (member.id),"Can't welcome you <@%s>.I'm busy napping" % (member.id),"Welcome we are serving your bottle <@%s>" % (member.id),"Welcome <@%s>! You win a dog and a broken hand!" % (member.id)]
    randNum = math.floor(randint(1, 5))
    await client.send_message(channel, randMessages[randNum])





client.run("NDA2NzYwMDIwNDUwMDgyODM2.DVG24w.gkYfCdaBYnSkRSvnEdZlqvqCIcY")
