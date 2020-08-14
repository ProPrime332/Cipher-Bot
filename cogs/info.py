import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import *

class info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='support')
    async def support(self, ctx):
        embed = discord.Embed(title="Support", description="For Support ", color=0x261a38)
        embed.add_field(name="꧁༒Prime༒꧂#0410", value="Ask him", inline=False)
        embed.add_field(name="Join Support server at ", value="https://discord.gg/SFcGP3F", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='invite')
    async def inv(self, ctx):
        embed = discord.Embed(title="Invite Link", description="https://discord.com/oauth2/authorize/?permissions=1341644481&scope=bot&client_id=742647318767075338", color=0x261a38)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))