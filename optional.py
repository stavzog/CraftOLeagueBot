import discord
from discord.ext import commands

class Extra():
    """Extra Bot Commands"""
	def __init__(self, bot):
		self.bot = bot
		
def setup(bot):
	bot.add_cog(Extra(bot))
