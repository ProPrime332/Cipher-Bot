import discord
from discord.ext import commands
import asyncio
from datetime import datetime
from random import randint
from discord.ext import menus

class MyMenu(menus.Menu):

    def __init__(self, bot : commands.Bot):
        super().__init__(check_embeds=True)
        self.bot = bot
        self.page = 0


    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed(title="Test", description="Ok i m testing")
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
