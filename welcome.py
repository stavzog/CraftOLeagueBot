import discord
from discord.ext import commands

class Optional():
	def __init__(self,bot):
		self.bot = bot

	async def on_member_join(member):
		channel = discord.utils.get(member.server.channels, name='welcome', type=discord.ChannelType.text)
		await client.change_nickname(member, "[Member]%s" % (member.name))
		randMessages = ["Welcome to our server <@%s>!" % (member.id),"Welcome to our firepit <@%s>" % (member.id),"Hey <@%s>, doorbell broken!Yell Ding Dong" % (member.id),"If our dog doesn't like u, we probbably won't either <@%s>" % (member.id),"<@%s> Beware of da... Aaam...Just beware!" % (member.id),"Well, <@%s> there is free wifi and pizza inside!" % (member.id),"Looks like the God of Thunder, <@%s>, might stay for a dinner" % (member.id),"Hallo <@%s>, please ring doorbell and run, the dog needs exercise!" % (member.id),"Welcome <@%s>, to our neck of da woods" % (member.id),"<@%s> Smile, the paparatsi are coming" % (member.id), "If you forgot to bring popcorn <@%s>, I 'll call the dog" % (member.id),"Come and see our campfire <@%s>, where friends and marshmellows become **Toasted**" % (member.id),"I’ve been waiting in the corner, with honor, for your coming, with your daughter! Welcome <@%s>" % (member.id),"Can't welcome you <@%s>.I'm busy napping" % (member.id),"Welcome we are serving your bottle <@%s>" % (member.id),"Welcome <@%s>! You win a dog and a broken hand!" % (member.id)]
		randNum = math.floor(randint(0, len(randMessages)-1))
		await client.send_message(channel, randMessages[randNum])

	async def on_member_remove(member):
		channel = discord.utils.get(member.server.channels, name='welcome', type=discord.ChannelType.text)
		randMsg = ["Life is a series of hellos and goodbyes. I'm afraid it's time for goodbye <@%s>" % (member.id),"Everybody has to leave, everybody has to leave their home and come back so they can love it again for all new reasons.Goodbye <@%s>" % (member.id),"This is not the end. It is not even the beginning of the end. But it is, perhaps, the end of the beginning.We must all goodbye <@%s> now" % (member.id),"After all we've been through, we finally have to goodbye <@%s> from %s" % (member.id,member.server.name)]
		randNum = math.floor(randint(0, len(randMsg)-1))
		await client.send_message(channel, randMsg[randNum])

def setup(bot):
	bot.add_cog(Optional(bot))
    
