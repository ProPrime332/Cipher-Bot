from discord.ext import commands
import discord

import itertools
from datetime import datetime as dt
from discord.ext import menus


class HelpMeu(menus.Menu):

    def __init__(self, bot : commands.Bot, ctx):
        super().__init__(timeout=30.0, delete_after_message=False, check_embeds=True)
        self.bot = bot
        self.page = 1
        self.ctx = ctx
        self.cogs = ctx.cogs
        self.pages = len(self.cogs) + 1

    def make_desc(self):
        desc = """Elite Help!
        Elite is a Moderation, Fun & Utility Bot.

        Use the Emojis Below to Change Pages.

        For More Info on a Command: #help <command>
        """ #TODO: change name
        counter = 1
        for cog in self.cogs:
            desc += f"**Page {counter}: {cog.emoji} {cog.qualified_name}"
        return desc

    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed(title="Cipher Help", description=self.make_desc(), timestamp=dt.now())
        embed.set_footer(text=f"Page {self.page} / {self.pages}")
        return await channel.send(embed=embed)

    @menus.button('\U0001f44d')
    async def on_thumbs_up(self, payload):
        new_embed = discord.Embed(title="Part 1", description="Ok boomer")
        await self.message.edit(embed=new_embed)

    @menus.button('\N{THUMBS DOWN SIGN}')
    async def on_thumbs_down(self, payload):
        embed = discord.Embed(title="U back")
        await self.message.edit(embed=embed)

    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        self.stop()
