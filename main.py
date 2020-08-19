from discord.ext import commands
import discord
from config import token, initial_cogs
from discord.ext.commands.errors import NoPrivateMessage, BadArgument, MissingRequiredArgument, CommandNotFound

from aiohttp import ClientSession
import datetime
import asyncio


class Helper(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=kwargs.pop('command_prefix', ['*']), case_insensitive=True, **kwargs)
        self.session = ClientSession(loop=self.loop)
        self.start_time = datetime.datetime.utcnow()
        self.clean_text = commands.clean_content(escape_markdown=True, fix_channel_mentions=True)

    """"  Events  """

    async def on_ready(self):
        print(f'Successfully logged in as {self.user}\nSharded to {len(self.guilds)} guilds')
        await self.change_presence(status=discord.Status.online, activity=discord.Game(name=f'use the prefix * | Watching {len(self.guilds)} servers.'))
        for ext in initial_cogs:
            self.load_extension(ext)

    async def process_commands(self, message):
        ctx = await self.get_context(message)
        if ctx.command is None:
            return
        if ctx.guild is None:
            await ctx.send("no commands in private messages")
        await self.invoke(ctx)

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        print(type(error))
        if isinstance(error, BadArgument):
            await ctx.send(f'Pls provide the correct arguments, for more info use {ctx.prefix}help')
            await ctx.send_help(ctx.command)
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f'Pls provide the required arguments, for more info use {ctx.prefix}help')
            await ctx.send_help(ctx.command)
        elif isinstance(error, CommandNotFound):
            await ctx.send("thats not a vaild command dude")
            await ctx.send_help()
        else:
            await ctx.send(f"command raised an error {error}")

    @classmethod
    async def setup(cls, **kwargs):
        bot = cls()
        try:
            await bot.start(token, **kwargs)
        except KeyboardInterrupt:
            await bot.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Helper.setup())
