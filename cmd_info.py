""" Info Command"""
from discord.ext import commands
import loadconfig


class InfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.cooldown(1, loadconfig.__cooldown__, commands.BucketType.user)
    async def info(self, ctx):
        await ctx.respond(
        """
        **Thank you** for using **MEMELORD**.
        
        This project is on **GitHub.com** (https://github.com/cybermyber/memelord)
        
        The project is based on the open-source projects **Pycord** (https://github.com/Pycord-Development/pycord) 
        and the **Meme_Api** by **D3vd** (https://github.com/D3vd/Meme_Api)
        
        Feel free to contribute to this project by creating a pull request.
        """
        )
