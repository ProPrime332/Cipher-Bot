from discord import Embed
import asyncpg
from discord.utils import get
from utils.utilities import utilities
from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import Cog, command, has_permissions, is_owner

def syntax(command):
	cmd_and_aliases = "|".join([str(command), *command.aliases])
	params = []

	for key, value in command.params.items():
		if key not in ("self", "ctx"):
			params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

	params = " ".join(params)

	return f"`{cmd_and_aliases} {params}`"

class HelpMenu(ListPageSource):
	def __init__(self, ctx, data):
		self.ctx = ctx

		super().__init__(data, per_page=3)

	async def write_page(self, menu, fields=[]):
		offset = (menu.current_page*self.per_page) + 1
		len_data = len(self.entries)

		embed = Embed(title="Help",
					  description="Welcome to the Moderation+ help dialog!",
					  colour=self.ctx.author.colour)
		embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
		embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands.")

		for name, value in fields:
			embed.add_field(name=name, value=value, inline=False)

		return embed

	async def format_page(self, menu, entries):
		fields = []

		for entry in entries:
			fields.append((entry.brief or "No description", syntax(entry)))

		return await self.write_page(menu, fields)

class Misc(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.db = utilities.guildsdatabase(self.bot.loop, "postgres", "li996748")

	async def cmd_help(self, ctx, command):
		embed = Embed(title=f"Help with `{command}`",
					  description=syntax(command),
					  colour=ctx.author.colour)
		embed.add_field(name="Command description", value=command.help)
		await ctx.send(embed=embed)

	@command(help="Sets the prefix for the current guild.")
	@has_permissions(manage_guild = True)
	async def setprefix(self, ctx, prefix:str):
		await self.db.fetch(f"UPDATE guilds SET prefix='{prefix}' WHERE guildid='{ctx.guild.id}'")
		await ctx.send(f"Set prefix to {prefix}!")

	@command(help="Evaluates code.")
	async def eval(self, ctx, *, code:str):
		pass

	@command(help="Shows this message.")
	async def help(self, ctx, cmd:str = None):
		"""Shows this message."""
		if cmd is None:
			menu = MenuPages(source=HelpMenu(ctx, list(self.bot.commands)),
							 delete_message_after=True,
							 timeout=60.0)
			await menu.start(ctx)

		else:
			if (command := get(self.bot.commands, name=cmd)):
				await self.cmd_help(ctx, command)

			else:
				await ctx.send("That command does not exist.")

	@is_owner()
	@command()
	async def tsql(self, ctx, *, sql: str) -> None:
		output = await self.db.fetch(sql)
		await ctx.send(f'```{output}```')


	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("Miscellaneous")

def setup(bot):
	bot.add_cog(Misc(bot))
