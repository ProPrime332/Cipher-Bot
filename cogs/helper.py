import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import *

class helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help-fun')
    async def helfun(self, ctx):
        embed = discord.Embed(title="Help", description="Here your help", color=0x261a38)
        embed.add_field(name="*kill", value="Kills the mentioned user", inline=True)
        embed.add_field(name="*choose", value="Settles the score someway", inline=True)
        embed.add_field(name="*dm", value="Dm's the specified user", inline=True)
        embed.add_field(name="*wow", value="Sends a wow image", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='support')
    async def support(self, ctx):
        embed = discord.Embed(title="Support", description="For Support ", color=0x261a38)
        embed.add_field(name="꧁༒Prime༒꧂#0410", value="Ask him", inline=False)
        embed.add_field(name="Join Support server at ", value="https://discord.gg/5r3rBKV", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='help-math')
    async def helmath(self, ctx):
        embed = discord.Embed(title="Help", description="Here your help", color=0x261a38)
        embed.add_field(name="*add", value="Adds the given 2 numbers", inline=True)
        embed.add_field(name="*multiply", value="Multiplies the given 2 numbers", inline=True)
        embed.add_field(name="*difference", value="Subtracts the given 2 numbers.", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='help')
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Here your help", color=0x261a38)
        embed.add_field(name="*help-fun", value="Gives Help for all fun commands.", inline=True)
        embed.add_field(name="*help-math", value="Gives Help for all math commands.", inline=True)
        embed.add_field(name="*support", value='Use this command if your doubt is not clear', inline=True)
        embed.add_field(name='*invite', value='Use this command if you want to invite bot to your server', inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='invite')
    async def inv(self, ctx):
        await ctx.send('Here my Invite link add me pls.')
        await ctx.send('\nhttps://discord.com/oauth2/authorize/?permissions=1341644481&scope=bot&client_id=742647318767075338')


def setup(bot):
    bot.add_cog(helper(bot))