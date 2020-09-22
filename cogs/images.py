import discord
from discord.ext import commands
import random
import pyfiglet
import praw


reddit = praw.Reddit(client_id = "KqUKz_3IJiHQTA",
                     client_secret = "HFAxvZsEE3S-UkoeBUNMMMx54p4",
                     user_agent = "Cipher")

class Imgs(commands.Cog):
    """Fun commands to enjoy the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.embed_colour = discord.Colour.from_rgb(66, 236, 245)

    @commands.command(name="dog")
    async def dog(self, ctx):
        """Sends a random dog image."""
        img = reddit.subreddit("dog").random()
        img = img.url
        embed=discord.Embed(title="A DOG", color=self.embed_colour)
        embed.set_image(url=img)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="cat")
    async def cat(self, ctx):
        """Sends a random cat image."""
        img = reddit.subreddit("cat").random()
        img = img.url
        embed=discord.Embed(title="A CAT", color=self.embed_colour)
        embed.set_image(url=img)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    #@commands.command(name="porn")
    #async def porn(self, ctx):
        #img = reddit.subreddit("porn").random()
        #img = img.url
        #embed = discord.Embed(title="Enjoy NSFW")
        #embed.set_image(url=img)
        #if ctx.channel.is_nsfw():
            #await ctx.send(embed=embed)
        #else:
            #await ctx.send("Channel should be NSFW to run this command.")

def setup(bot):
    bot.add_cog(Imgs(bot))
