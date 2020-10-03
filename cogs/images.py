import discord
from discord.ext import commands
import random
import pyfiglet
import praw
from datetime import datetime
from cogs.lol import MyMenu


reddit = praw.Reddit(client_id = "KqUKz_3IJiHQTA",
                     client_secret = "HFAxvZsEE3S-UkoeBUNMMMx54p4",
                     user_agent = "Cipher")

class Imgs(commands.Cog):
    """Fun commands to enjoy the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.embed_colour = discord.Colour.from_rgb(66, 236, 245)
        self.emoji = '📷'

    @commands.command(name="dog")
    async def dog(self, ctx):
        """Sends a random dog image."""
        img = reddit.subreddit("dog").random()
        img = img.url
        embed=discord.Embed(title="A DOG", color=self.embed_colour, timestamp=datetime.utcnow())
        embed.set_image(url=img)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author}')
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="cat")
    async def cat(self, ctx):
        """Sends a random cat image."""
        img = reddit.subreddit("cat").random()
        img = img.url
        embed=discord.Embed(title="A CAT", color=self.embed_colour, timestamp=datetime.utcnow())
        embed.set_image(url=img)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author}')
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def me(self, ctx):
        m = MyMenu(self.bot)
        await m.start(ctx)

def setup(bot):
    bot.add_cog(Imgs(bot))
