import discord
from discord.ext import commands
from discord.ext.commands.errors import BadArgument


class CommandErrorHandler(commands.cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f'Pls provide the required arguments, for more info use {self.clean_prefix}help')


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
