import discord
from discord.ext import commands
import random
import pyfiglet
import praw
import discord
from datetime import datetime



reddit = praw.Reddit(client_id = "KqUKz_3IJiHQTA",
                     client_secret = "HFAxvZsEE3S-UkoeBUNMMMx54p4",
                     user_agent = "Cipher")



class fun(commands.Cog):
    """Fun commands to enjoy the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.embed_colour = discord.Colour.from_rgb(252, 102, 0)
        self.emoji = '🎪'

    @commands.command(name='choose', help='Settles the score someway')
    async def choose(self, ctx, *choices):
        """Settles the score someway."""
        await ctx.send(random.choices(choices)[0])
        await ctx.message.delete()

    @commands.command(name='kill', help='Gives a random kill response.')
    async def kill(self, ctx, *, user : discord.User):
        """Gives a random kill response."""
        kills = [f"{user.mention} slips bleach into {ctx.author.mention}'s lemonade.",
                 f"{user.mention} dies of natural causes.",
                 f"{user.mention} dies from bad succ.",
                 f"{user.mention} dies from dabbing too hard.",
                 f"{user.mention} dies from posting normie memes.",
                 f"{user.mention} dies from disrespecting wahmen.",
                 f"{user.mention} dies from watching the emoji movie and enjoying it.",
                 f"{user.mention} hired me to kill you, but I don't want to! $mention",
                 f"{user.mention} slips on a banana peel and falls down the stairs.",
                 f"{ctx.author.mention} murders {user.mention} with an axe.",
                 f"{ctx.author.mention} pressed delete. It deleted {user.mention}",
                 f"{user.mention} dies because they used a bobby pin to lift their eyelashes",
                 f"{user.mention} dies because they were just too angry.",
                 f"{user.mention} decided it was a good idea to fight a tiger while smelling like meat. It did not end well.",
                 f"{user.mention} disappeared from the universe.",
                 f"{user.mention} drank some toxic soda before it was recalled.",
                 f"{user.mention} was killed by $author with baby wipes.",
                 f"{user.mention} dies in a horrible accident, and it was engineered by {ctx.author.mention}.",
                 f"{user.mention} dies of starvation."]
        embed = discord.Embed(title=f"**{ctx.author} killed {user}**", description=random.choices(kills)[0])
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name='dm')
    async def dm(self, ctx, user: discord.User, *, message):
        """Sends the specified user a DM."""
        await user.send(f'{message}\n\n**{ctx.author}**')
        await ctx.send(f'Sent a message to {user}')
        await ctx.message.delete()

    @commands.command(name="meme")
    async def meme(self, ctx):
        """ Sends a meme """
        img = reddit.subreddit("meme").random()
        img = img.url
        embed = discord.Embed(title="A meme", color=self.embed_colour, timestamp=datetime.utcnow())
        embed.set_image(url=img)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name='wow')
    async def wow(self, ctx):
        """Sends a WOW gif."""
        wows = ['https://tenor.com/view/yawnface-gif-4425271', 'https://tenor.com/view/wow-ted-gif-4233186']
        embed = discord.Embed(title="Wow", color=self.embed_colour)
        embed.set_image(url=random.choices(wows)[0])
        await ctx.send(embed=embed)

    @commands.command(name='green', aliases=['gt', '>'])
    async def green(self, ctx, *, args):
        """sends greentext of the args"""
        await ctx.send(f"```css\n{args}```")
        await ctx.message.delete()

    @commands.command(name='ascii')
    async def ascii(self, ctx, *, inp: str):
        inp = pyfiglet.figlet_format(inp)
        await ctx.send(f'```{inp}```')
        await ctx.message.delete()

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
        embed = discord.Embed(title=f"**The 8ball has spoken**", description=random.choices(responses)[0])
        await ctx.send(embed=embed)
        await ctx.message.delete()
    @commands.command(name='insult')
    async def insult(self, ctx, *, user : discord.User):
        """Insults the mentioned user"""
        roasts = ['I\'d slap you but it would be animal abuse.',
                  'I thoguht you were a piece of shite but ur discord smells like it has been shitted over',
                  'were you born this stupid or did you take lessons?',
                  'The pitch of your voice drives dogs insane',
                  'You know, one of the many, many things that confuses me about you is that you remain unmurdered.',
                  'A nose job? I think you need a nose career at this rate',
                  'You are your own hate crime',
                  'You are what happens when urine gets mixed with the sperm',
                  'I wonder if you\'d be able to speak more clearly if your parents were second cousins instead of first.',
                  'I\'d love to stay and chat but I\'d rather have type-2 diabetes',
                  'Were you born a cunt, or is it something you have to recommit yourself to every morning?',
                  'I shouldn\'t roast you, I can\'t imagine the pain you go through with that face!',
                  'By the looks of it, you\'ve had enough cake days',
                  'Not even your dog loves you. He\'s just faking it.',
                  'Next time, don\'t take a laxative before you type because you just took a steaming stinking dump right on the page. Now wipe that shit up and don\'t fuck it up like your life.',
                  'You definitely peg yourself',
                  'I’m betting your keyboard is filthy as fuck now from all that Cheeto-dust finger typing, you goddamn weaboo shut in.',
                  'WHY SHOULD I LISTEN TO YOU ARE SO FAT THAT YOU CAN\'T POO OR PEE YOU STINK LYRE YOU HAVE A CRUSH ON POO',
                  'I curse the vagina that farted you out.']
        embed = discord.Embed(title=f"**{ctx.author} roasted {user}**", description=random.choices(roasts)[0])
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(fun(bot))
