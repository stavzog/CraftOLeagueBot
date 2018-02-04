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
            await ctx.say(randMsg)
        elif randMsg == "I want":
            randBits = random.choice(msgbits2)
            randMsg = randMsg + " " + randBits
            await ctx.say(randMsg)
        elif randMsg == "I hope":
            randBits = random.choice(msgbits3)
            randMsg = randMsg + " " + randBits
            await ctx.say(randMsg)
        else:
            await ctx.say(randMsg)

def setup(bot):
    bot.add_cog(Extra(bot))

