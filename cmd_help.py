""" Help command for the bot. """
from discord import Embed
from discord.ext import commands
import loadconfig


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.cooldown(1, loadconfig.__cooldown__, commands.BucketType.user)
    async def help(self, ctx):
        embed = Embed(title="MEMELORD HELP", type="rich", colour=0x992D22)
        embed.add_field(name="/help", value="Shows this message.", inline=False)
        embed.add_field(name="/meme", value="Random meme!", inline=False)
        embed.add_field(
            name="/random subreddit:<Subreddit>",
            value="Random image from your favorite subreddit. \n e.g. /random subreddit:gaming",
            inline=False,
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/751428074201153557/c03bc4da3d76d1161c891f6eb5a87442.png"
        )
        await ctx.respond(embed=embed)
