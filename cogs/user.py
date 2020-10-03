from discord.ext import commands
import discord

class Users(commands.Cog):
    """Commands to get info about user."""

    def __init__(self, bot):
        self.bot = bot
        self.emoji = '🧑'

    @commands.command(name='avatar', aliases=['av'])
    async def avatar(self, ctx,  *,  member : discord.Member = None):
        member = member or ctx.author
        """Displays the avatar of mentioned user."""
        avatar_user = member.avatar_url
        embed = discord.Embed(title=f"{member}'s avatar")
        embed.set_image(url=avatar_user)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Users(bot))
