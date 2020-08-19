import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import *

class info(commands.Cog):
    " " " INFO about the bot to help users. " " "

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='support')
    async def support(self, ctx):
        " " " Link to support server. " " "
        embed = discord.Embed(title="Support", description="For Support ", color=0x261a38)
        embed.add_field(name="꧁༒Prime༒꧂#0410", value="Ask him", inline=False)
        embed.add_field(name="Join Support server at ", value="https://discord.gg/6nG92Rc", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='invite')
    async def inv(self, ctx):
        " " " Invite link  of the bot. " " "
        embed = discord.Embed(title="Invite Link", description="https://discord.com/oauth2/authorize/?permissions=1341644481&scope=bot&client_id=742647318767075338", color=0x261a38)
        await ctx.send(embed=embed)

    @commands.command(name='dev')
    async def dev(self, ctx):
        " " " Info about developers of the bot. " " "
        embed = discord.Embed(title='Devs', description='This bot is developerd by Prime and ceres.')
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        " " " Info about developers of the bot. " " "
        embed = discord.Embed(title='Ping', description=f'Here is your Ping:\n```{round(self.bot.latency * 1000)}ms```')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
