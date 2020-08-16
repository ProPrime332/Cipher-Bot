import discord
from discord.ext import commands
from discord.ext.commands.errors import BadArgument
from discord.ext.commands.errors import MissingRequiredArgument


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f'Pls provide the correct arguments, for more info use {ctx.prefix}help')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'Pls provide the required arguments, for more info use {ctx.prefix}help')


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
