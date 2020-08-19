from discord.ext import commands
import discord

class Users(commands.Cog):
    """Commands to get info about user."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar', aliases=['av'])
    async def avatar(self, ctx,  *,  member : discord.Member):
        """Displays the avatar of mentioned user."""
        avatar_user = member.avatar_url
        await ctx.send(str(avatar_user))

def setup(bot):
    bot.add_cog(Users(bot))
