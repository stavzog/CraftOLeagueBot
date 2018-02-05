import discord
from discord.ext import commands
import random

class Extra():
    """Extra bot commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def randmsg(self, ctx):
        msgbits1 = [
        "a noob.","lolin' my life.",
        "bored of not using me bro.","a very clever bot.",
        "looking for someone to type `:help`."]
        msgbits2 = [
        "some oil for my gears.",
        "u to type a command!.","u to help me code.",
        "someone brave enough to join here: https://discord.gg/gFuac2r","sb to fix my gears!"]
        msgbits3 = [
        "u haven't just got out of the mistletoe","I could love one day"]
        msgs = [
        "Im",
        "I want",
        "I hope",
        "I found a new friend!",
        "Looks like there is an anxious user!",
        "A bird in the sky!",
        "Who turned off the lights :(",
        "Hate it when no onew uses me",
        "Type :help to see all my commands",
        "Did u know that the server owner could load new plugins",
        "Like being a bot",
        "Isn't it amazing that",
        "Like my commands?"]
        randMsg = random.choice(msgs)
        if randMsg == "Im":
            randBits = random.choice(msgbits1)
            randMsg = randMsg + " " + randBits
            await self.bot.say(randMsg)
        elif randMsg == "I want":
            randBits = random.choice(msgbits2)
            randMsg = randMsg + " " + randBits
            await self.bot.say(randMsg)
        elif randMsg == "I hope":
            randBits = random.choice(msgbits3)
            randMsg = randMsg + " " + randBits
            await self.bot.say(randMsg)
        else:
            await self.bot.say(randMsg)

    @commands.command(pass_context=True)
    async def conmb(ctx):
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
    @commands.command(pass_context=True)
    async def encode(ctx, *, msg):
        encoded = []
        msg = msg.lower()
        for letter in msg:
            randnum = randint(0, len(msg)-1)
            if letter == "i":
                letter = "1"
                encoded.append(letter)
            elif letter == "a":
                letter = "@"
                encoded.append(letter)
            elif letter == "e":
                letter = "3"
                encoded.append(letter)
            elif letter == "o":
                letter = "0"
                encoded.append(letter)
            else:
                if msg[randint] == letter:
                    letter = letter.upper()
                    encoded.append(letter)
        await client.say("Encoded message:{}".format(" ".join(encoded)))
    

def setup(bot):
    bot.add_cog(Extra(bot))
