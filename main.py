"""Main file for the bot"""
from discord import Game
from discord.ext import commands
from cmd_random import RandomCommand
from cmd_help import HelpCommand
from cmd_meme import MemeCommand
from cmd_info import InfoCommand
import loadconfig

bot = commands.Bot(activity=Game(name=loadconfig.__activity__))
bot.add_cog(RandomCommand(bot))
bot.add_cog(HelpCommand(bot))
bot.add_cog(MemeCommand(bot))
bot.add_cog(InfoCommand(bot))
bot.run(loadconfig.__discord_token__)
