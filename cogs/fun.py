import discord
from discord.ext import commands
import random
import pyfiglet


class fun(commands.Cog):
    """Fun commands to enjoy the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='choose', help='Settles the score someway')
    async def choose(self, ctx, *choices):
        """Settles the score someway."""
        await ctx.send(random.choices(choices)[0])

    @commands.command(name='kill', help='Gives a random kill response.')
    async def kill(self, ctx, *, user : discord.User):
        """Gives a random kill response."""
        await ctx.send(f"Ooh you killed {user}")

    @commands.command(name='dm')
    async def dm(self, ctx, user: discord.User, *, message):
        """Sends the specified user a DM."""
        await user.send(f'{ctx.author} has a message for you *:{message}*')
        await ctx.send(f'Sent a message to {user}')

    @commands.command(name='wow')
    async def wow(self, ctx):
        """Sends a WOW gif."""
        wows = ['https://tenor.com/view/yawnface-gif-4425271', 'https://tenor.com/view/wow-ted-gif-4233186']
        await ctx.send(random.choices(wows)[0])

    @commands.command(name='green', aliases=['gt', '>'])
    async def green(self, ctx, *, args):
        """sends greentext of the args"""
        await ctx.send(f"```css\n{args}```")

    @commands.command(name='ascii')
    async def ascii(self, ctx, *, inp: str):
        inp = pyfiglet.figlet_format(inp)
        await ctx.send(f'```{inp}```')

    @commands.command(name='8ball')
    async def ball(self, ctx, *, response):
        """Brings the 8ball magic to discord"""
        responses = ['Cannot predict now.',
                     ' Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.'
                     ]
        await ctx.send(random.choices(responses)[0])

    @commands.command(name='insult')
    async def insult(self, ctx, *, user : discord.User):
        """Insults the mentioned user"""
        await ctx.send(f'I\'d slap you {user} but it would be animal abuse.')


def setup(bot):
    bot.add_cog(fun(bot))
