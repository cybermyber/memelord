""" Command to get a random meme from Reddit. """
from aiohttp import ClientSession
from discord import Embed
from discord.ext import commands
import loadconfig

class MemeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.memeapi = loadconfig.__apiurl__

    @commands.slash_command()
    @commands.cooldown(1, loadconfig.__cooldown__, commands.BucketType.user)
    async def meme(self, ctx):
        async with ClientSession() as session:
            async with session.get(f"{self.memeapi}") as resp:
                data = await resp.json()
        if data is None:
            await ctx.respond("Sorry, no memes found or API is down.", ephemeral=True)
            return
        if data["nsfw"] and not ctx.channel.is_nsfw():
            embed = self.create_nsfw_embed()
            await ctx.respond(embed=embed)
            return
        embed = self.create_embed(data)
        await ctx.respond(embed=embed)

    @meme.error
    async def random_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(
                f"You are on cooldown. Try again in {int(error.retry_after)}s.",
                ephemeral=True,
            )

    def create_embed(self, data):
        url = data["url"]
        title = data["title"]
        author = data["author"]
        upvotes = data["ups"]
        postlink = data["postLink"]
        subreddit = data["subreddit"]
        embed = Embed(title=title, url=postlink, type="rich", colour=0x71368A)
        embed.set_image(url=url)
        embed.set_footer(
            icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png",
            text=subreddit + " | ▲ " + str(upvotes),
        )
        embed.set_author(name=author)
        return embed

    def create_nsfw_embed(self):
        image = "https://i.imgur.com/LmzRs8Y.png"
        title = "Attention!"
        description = """This image is marked as Not Safe For Work (NSFW).
        Please use a channel marked as NSFW if the subreddit is also NSFW. 
        If not, please try the command again."""
        embed = Embed(
            title=title, type="rich", colour=0x992D22, description=description
        )
        embed.set_thumbnail(url=image)
        return embed
