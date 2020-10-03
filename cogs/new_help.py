from discord.ext import commands
import discord

import itertools
from datetime import datetime as dt
from discord.ext import menus


class HelpMenu(menus.Menu):

    def __init__(self, bot: commands.Bot, ctx):
        super().__init__(timeout=30.0, delete_message_after=False)
        self.bot = bot
        self.page = 1
        self.ctx = ctx
        self.cogs = list(bot.cogs.values())
        self.pages = len(self.cogs) + 1

    def make_desc(self):
        desc = """Elite Help!
Elite is a Moderation, Fun & Utility Bot.

Use the Emojis Below to Change Pages.

For More Info on a Command: #help <command>
""" #TODO: change name
        counter = 1
        for cog in self.cogs:
            desc += f"**Page {counter}**: {cog.qualified_name.capitalize()}\n"
            counter +=1
        return desc

    def cog_embed(self):
        cog = self.cogs[self.page-2]
        desc = ""
        for command in cog.get_commands():
            desc += f"❯ {command.name}: `{command.help or 'no help provided'}`\n"
        embed = discord.Embed(title=f"**{cog.qualified_name.capitalize()} Help**", timestamp=dt.now(), description=desc)
        embed.set_footer(text=f"Page {self.page} / {self.pages}")
        return embed

    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed(title="Cipher Help", description=self.make_desc(), timestamp=dt.now())
        embed.set_footer(text=f"Page {self.page} / {self.pages}")
        return await channel.send(embed=embed)


    @menus.button("\U00002b05")
    async def on_thumbs_down(self, payload):
        self.page -= 1
        if self.page == 0:
            await self.message.edit("Page 0 doesn't exit :(")
        await self.message.edit(embed=self.cog_embed())

    @menus.button('\U000027a1')
    async def on_right_arrow(self, payload):
        self.page += 1
        if self.page > self.pages:

            await self.message.edit("That was the last page bub")
        else:
            await self.message.edit(embed=self.cog_embed())

    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        self.stop()


class Help(commands.HelpCommand):
    def __init__(self, **options):
        super().__init__(verify_checks=True, **options)

    def embedify(self, title: str, description: str) -> discord.Embed:
        """Returns the default embed used for our HelpCommand"""
        embed = discord.Embed(title=title, description=description, color=0x36393E, timestamp=dt.utcnow())
        embed.set_author(name="Cipher | Help", icon_url=self.context.bot.user.avatar_url)
        embed.set_footer(icon_url=self.context.bot.user.avatar_url, text=f'{self.context.bot.user.name}')
        return embed

    def command_not_found(self, string) -> str:
        return f'Command or category `{self.clean_prefix}{string}` not found. Try again...'

    def subcommand_not_found(self, command, string) -> str:
        ret = f"Command `{self.context.prefix}{command.qualified_name}` has no subcommands."
        if isinstance(command, commands.Group) and len(command.all_commands) > 0:
            return ret[:-2] + f' named {string}'
        return ret

    @staticmethod
    def no_category() -> str:
        return 'No Category'

    def get_opening_note(self) -> str:
        return f"""
                   Use **`{self.clean_prefix}help "command name"`** for more info on a command
                """

    @staticmethod
    def command_or_group(*obj):
        names = []
        for command in obj:
            if isinstance(command, commands.Group):
                names.append(f'*{command.name}*')
            else:
                names.append(f'*{command.name}*')
        return names

    def full_command_path(self, command, include_prefix: bool = False):
        string = f'{command.qualified_name} {command.signature}'

        if any(command.aliases):
            string += ' | Aliases: '
            string += ', '.join(f'`{alias}`' for alias in command.aliases)

        if include_prefix:
            string = self.clean_prefix + string

        return string

    async def send_bot_help(self, mapping):
        menu = HelpMenu(self.context.bot, self.context)
        await menu.start(self.context)

    async def send_group_help(self, group):
        embed = self.embedify(title=self.full_command_path(group),
                              description=group.short_doc or "*No special description*")

        filtered = await self.filter_commands(group.commands, sort=True, key=lambda c: c.name)
        if filtered:
            for command in filtered:
                name = self.full_command_path(command)
                if isinstance(command, commands.Group):
                    name = 'Group: ' + name

                embed.add_field(name=name, value=command.help or "*No specified command description.*", inline=False)

        if len(embed.fields) == 0:
            embed.add_field(name='No commands', value='This group has no commands?')

        await self.context.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = self.embedify(title=cog.qualified_name, description=cog.description or "*No special description*")

        filtered = await self.filter_commands(cog.get_commands())
        if filtered:
            for command in filtered:
                name = self.full_command_path(command)
                if isinstance(command, commands.Group):
                    name = 'Group: ' + name

                embed.add_field(name=name, value=command.help or "*No specified command description.*", inline=False)

        await self.context.send(embed=embed)

    async def send_command_help(self, command):
        embed = self.embedify(title=self.full_command_path(command, include_prefix=True),
                              description=command.help or "*No specified command description.*")

        # Testing purposes only.
        try:
            await command.can_run(self.context)
        except Exception as error:
            error = getattr(error, 'original', error)

            if isinstance(error, commands.MissingPermissions):
                missing_permissions = error.missing_perms
            elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
                missing_permissions = error.missing_roles or [error.missing_role]
            else:
                await self.context.bot.get_user(488278979900342282).send(
                    f'send_command_help\n\n{self.context.author} raised this error that you didnt think of:\n'
                    f'{type(error).__name__}\n\nChannel: {self.context.channel.mention}'
                )
                missing_permissions = None

            if missing_permissions is not None:
                embed.add_field(name='You are missing these permissions to run this command:',
                                value=self.list_to_string(missing_permissions))

        await self.context.send(embed=embed)

    @staticmethod
    def list_to_string(_list):
        return ', '.join([obj.name if isinstance(obj, discord.Role) else str(obj).replace('_', ' ') for obj in _list])


class NewHelp(commands.Cog, name="Help Command"):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = Help()
        bot.help_command.cog = self
        bot.get_command('help').hidden = True
        self.bot = bot

    def cog_unload(self):
        self.bot.help_command = self._original_help_command


def setup(bot):
    bot.add_cog(NewHelp(bot))
