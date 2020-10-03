from discord.ext import commands
import discord

class Math(commands.Cog):
    """Maths Commands to help you."""

    def __init__(self, bot):
        self.bot = bot
        self.emoji = '➗'
    @commands.command(name='add', help='Adds 2 given numbers.')
    async def asu(self, ctx, number1: int, number2: int = 0):
        """Adds the 2 numbers given."""
        su = (number1 + number2)
        await ctx.send(su)

    @commands.command(name='multiply', aliases=['mult', 'multi', 'product'], help='Multiplies 2 given numbers.')
    async def mult(self, ctx, number1: int, number2: int = 0):
        """""Multiplies the 2 numbers given."""
        su = (number1 * number2)
        await ctx.send(su)

    @commands.command(name='difference', aliases=['subtract', 'minus', 'diff'], help='Subtracts 2 given numbers.')
    async def difference(self, ctx, number1: int, number2: int = 0):
        """Subtracts the 2 numbers given."""
        su = abs(number1 - number2)
        await ctx.send(su)

    @commands.command(name='odd-even', aliases=['odd', 'even'])
    async def odeve(self, ctx, number: int):
        """Tells weather the given number is odd or even."""
        if number % 2 == 0:
            await ctx.send('Your Number is even')
        else:
            await ctx.send('Your Number is odd')


def setup(bot):
    bot.add_cog(Math(bot))
