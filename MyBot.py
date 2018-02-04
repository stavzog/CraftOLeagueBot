import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from random import *
import math

Client = discord.Client()
client = commands.Bot(command_prefix = ":")

# this specifies what extensions to load when the bot starts up
startup_extensions = ["welcome"]

@client.event
async def on_ready():
    print("Bot is running! GG")
    await client.change_presence(game=discord.Game(name='with :help'))


@client.command(pass_context=True)
async def member(ctx, user: discord.Member):
    """Dispaly info about the member"""
    await client.say("The users name is: {}".format(user.name))
    await client.say("The users ID is: {}".format(user.id))
    await client.say("The users status is: {}".format(user.status))
    await client.say("The users highest role is: {}".format(user.top_role))
    await client.say("The user joined at: {}".format(user.joined_at))

@client.command(pass_context=True)
async def load(ctx, extension_name : str):
    """Loads an extension."""
    role = discord.utils.get(ctx.message.server.roles,name="Owner")
    if role.id in [role.id for role in ctx.message.author.roles]:
    	try:
    		client.load_extension(extension_name)
    	except (AttributeError, ImportError) as e:
    		await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
    		return
    	await client.say("{} loaded.".format(extension_name))
    else:
        await client.say("You don't have permission to use this command!")
	
    

@client.command(name='reload', hidden=True, pass_context=True)
async def _reload(self, *, module : str):
    """Reloads a module."""
	role = discord.utils.get(ctx.message.server.roles,name="Owner")
   	if role.id in [role.id for role in ctx.message.author.roles]:
   		try:
			client.unload_extension(module)
			client.load_extension(module)
		except Exception as e:
			await client.say('\N{PISTOL}')
			await client.say('{}: {}'.format(type(e).__name__, e))
		else:
			await client.say('\N{OK HAND SIGN}')
	else:
		await client.say("You don't have permission to use this command!")
		


@client.command(pass_context=True)
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    role = discord.utils.get(ctx.message.server.roles,name="Owner")
    if role.id in [role.id for role in ctx.message.author.roles]:
        client.unload_extension(extension_name)
        await client.say("{} unloaded.".format(extension_name))

@client.command(pass_context=True)
async def owner(ctx):
    """Return the server owner"""
    server_owner = ctx.message.server.owner.id
    await client.say("The **owner** of this current server is <@{}> !".format(server_owner))

@client.command(pass_context=True)
async def announce(ctx, *, msg):
    """Sends a message to the announcements channel"""
    role = discord.utils.get(ctx.message.server.roles,name="Announcer")
    if role.id in [role.id for role in ctx.message.author.roles]:
        userID = ctx.message.author.id
        channel = discord.utils.get(ctx.message.server.channels, name="announcements", type=discord.ChannelType.text)
        await client.send_message(channel, "` \n {} \n ` ".format(' '.join(msg)))
        embed=discord.Embed(title="Msg sent", description="Your message was successfully sent", color=0x06ce97)
        embed.set_author(name=client.user.name,url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
        embed.add_field(name="Message:", value=msg, inline=False)
        await client.say(embed=embed)
    else:
        userID = ctx.message.author.id
        await client.say("<@{}> you do not have permission to use this command :(".format(userID))
@announce.error
async def announce_on_error(ctx, error):
    await client.say("Ooops, check your spelling! \n `:announce [msg]`")

@client.command(pass_context=True)
async def nick(ctx, *, nickname):
    """Changes nickname """
    await client.change_nickname(ctx.message.author, nickname)
    embed=discord.Embed(title="Nick changed", description="Your nickname was successfully changed", color=0x06ce97)
    embed.set_author(name=client.user.name,url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
    embed.add_field(name="Nickname", value=nickname, inline=False)
    await client.send_message(message.channel, embed=embed)
@nick.error
async def nick_on_error(ctx, error):
    await client.say("Ooops, check your spelling! \n `:nick [nickname]`")

@client.command(pass_context=True)
async def serverinfo(ctx):
    """Gives info about the server"""
    memberCount = 0
    x = ctx.message.server.members
    for member in x:
        memberCount = memberCount + 1
    embed=discord.Embed(title="Server Info", color=0x06ce97)
    embed.set_author(name=client.user.name, url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Owner", value=ctx.message.server.owner.name, inline=True)
    embed.add_field(name="Members", value=memberCount, inline=True)
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def cmembers(ctx):
    """Counts all the members(bots too)"""
    memberCount = 0
    x = ctx.message.server.members
    for member in x:
        memberCount = memberCount + 1
    await client.say("There are {} in your server (with bots)".format(memberCount))

@client.command(pass_context=True)
async def binfo(ctx):
    """Displayes bot info"""
    embed=discord.Embed(title="Bot Info", description="Some information about the bot", color=0x7d7d7d)
    embed.set_author(name=client.user.name,url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
    embed.add_field(name="Creator:", value="The creator of the bot is <@398580757335113739>", inline=False)
    embed.add_field(name="Made for:", value="The bot was originally made for a discord server called Craft O' League", inline=False)
    await client.say( embed=embed)

@client.command(pass_context=True)
async def clear(ctx):
    """Clears all the messages of current channel"""
    tmp = await client.send_message(ctx.message.channel, 'Clearing messages')
    async for msg in client.logs_from(ctx.message.channel):
        await client.delete_message(msg)

@client.command(pass_context=True)
async def setup(ctx):
    """Instructions on how to setup the bot"""
    embed=discord.Embed(title="Setting up", description="Bot setup", color=0x9e6701)
    embed.set_author(name=client.user.name,url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
    embed.add_field(name="Step 1.", value="You must have an announcements txt channel", inline=False)
    embed.add_field(name="Step 2.", value="You must have an Announcer role (capitalization counts)", inline=True)
    embed.add_field(name="Step 3.", value="You must have a welcome channel", inline=True)
    embed.set_footer(text="None of the above can be turned off!")
    await client.say(embed=embed) 

@client.command(pass_context=True)
async def invitelink(ctx):
    await client.say("Link: \n https://discordapp.com/oauth2/authorize?client_id=406760020450082836&scope=bot&permissions=2146958591 \n =========================== \n Join my server: https://discord.gg/gFuac2r \n")

@client.command(pass_context=True)
async def msg(ctx, chnl, *, cont):
    """Sends a message to a specific channel"""
    role = discord.utils.get(ctx.message.server.roles,name="Announcer")
    if role.id in [role.id for role in ctx.message.author.roles]:
        channel = discord.utils.get(ctx.message.server.channels, name=chnl, type=discord.ChannelType.text)
        await client.send_message(channel, "{}".format(cont))
        embed=discord.Embed(title="Msg sent", description="Your message was successfully sent", color=0x06ce97)
        embed.set_author(name=client.user.name,url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
        embed.add_field(name="Message:", value=msg, inline=False)
        await client.say(embed=embed)
@msg.error
async def msg_on_error(ctx, error):
    await client.say("Ooops, check your spelling! \n `:msg [channel] [message]`")

@client.command(pass_context=True)
async def rnum(ctx, ammount):
    """Returns rundom numbers"""
    global randnums
    randnums = []
    count = int(float(ammount))
    for x in range(count):
        x = math.floor(randint(1,9))
        x = str(x)
        randnums.append(x)
    await client.say("` \n Random Numbers: {} \n `".format(' '.join(randnums)))
@rnum.error
async def rnum_on_error(ctx,error):
    await client.say("Ooops, check your spelling! \n `:rnum [how many]`")

@client.command(pass_context=True)
async def code(ctx, *, msg):
    """Makes an embed"""
    embed=discord.Embed(description="{}".format(msg), color=0x008080)
    embed.set_author(name=ctx.message.author.name,icon_url=ctx.message.author.avatar_url)
    await client.say(embed=embed)
@code.error
async def code_on_error(ctx, error):
    await client.say("Ooops, check your spelling! \n `:code [msg]`")

@client.command(pass_context=True)
async def ocontact(ctx, *, msg):
    """Sends private message to the server owner"""
    embed=discord.Embed(description="{}".format(msg), color=0x008080)
    embed.set_author(name=ctx.message.author.name,icon_url=ctx.message.author.avatar_url)
    await client.send_message(ctx.message.author.server.owner, embed=embed)
    embed=discord.Embed(title="Msg sent", description="Your message was successfully sent", color=0x06ce97)
    embed.set_author(name=client.user.name,url="https://discord.gg/gFuac2r", icon_url=client.user.avatar_url)
    embed.add_field(name="Message:", value=msg, inline=False)
    await client.say(embed=embed)
@ocontact.error
async def ocontact_on_error(ctx,error):
    await client.say("Ooops, check your spelling! \n `:ocontact [msg]`")
    
@client.command(pass_context=True)
async def conmembers(ctx):
    """Returns all members connected to a voice channel""" 
    x = ctx.message.server.members
    conmembs = []
    for member in x:
        if member.voice_channel != None:
            conmembs.append(member.name)
            
    if conmembs == []:
        await client.say("No members are connected to a voice channel")
    else:
        await client.say("{}".format(" ".join(conmembs)))
        
for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    
    
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.server.channels, name='welcome', type=discord.ChannelType.text)
    await client.change_nickname(member, "[Member]{}".format(member.name))
    randMessages = ["Welcome to our server <@{}>!".format(member.id),"Welcome to our firepit <@{}>".format(member.id),"Hey <@{}>, doorbell broken!Yell Ding Dong".format(member.id),"If our dog doesn't like u, we probbably won't either <@{}>".format(member.id),"<@{}> Beware of da... Aaam...Just beware!".format(member.id),"Well, <@{}> there is free wifi and pizza inside!".format(member.id),"Looks like the God of Thunder, <@{}>, might stay for a dinner".format(member.id),"Hallo <@{}>, please ring doorbell and run, the dog needs exercise!".format(member.id),"Welcome <@{}>, to our neck of da woods".format(member.id),"<@{}> Smile, the paparatsi are coming".format(member.id), "If you forgot to bring popcorn <@{}>, I 'll call the dog".format(member.id),"Come and see our campfire <@{}>, where friends and marshmellows become **Toasted**".format(member.id),"I’ve been waiting in the corner, with honor, for your coming, with your daughter! Welcome <@{}>".format(member.id),"Can't welcome you <@{}>.I'm busy napping".format(member.id),"Welcome we are serving your bottle <@{}>".format(member.id),"Welcome <@{}>! You win a dog and a broken hand!".format(member.id)]
    randNum = math.floor(randint(0, len(randMessages)-1))
    await client.send_message(channel, randMessages[randNum])

    
     

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.server.channels, name='welcome', type=discord.ChannelType.text)
    randMsg = ["Life is a series of hellos and goodbyes. I'm afraid it's time for goodbye <@{}>".format(member.id),"Everybody has to leave, everybody has to leave their home and come back so they can love it again for all new reasons.Goodbye <@{}>".format(member.id),"This is not the end. It is not even the beginning of the end. But it is, perhaps, the end of the beginning.We must all goodbye <@{}> now".format(member.id),"After all we've been through, we finally have to goodbye <@{}> from {}".format(member.id, member.server.name)]
    randNum = math.floor(randint(0, len(randMsg)-1))
    await client.send_message(channel, randMsg[randNum])
    


client.run("NDA2NzYwMDIwNDUwMDgyODM2.DVG24w.gkYfCdaBYnSkRSvnEdZlqvqCIcY")
