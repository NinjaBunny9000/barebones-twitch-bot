import logging

from squak.constants import GREETING
from squak.constants import NICK
from squak.constants import PREFIX
from twitchio.ext import commands

log = logging.getLogger(__name__)


def make(irc_token, client_id, channel, conf):
    """
    Create and return the bot.
    """
    nick = conf.get("nick", NICK)
    bot = commands.Bot(
        irc_token=irc_token,
        client_id=client_id,
        nick=nick,
        prefix=conf.get("prefix", PREFIX),
        initial_channels=[channel],
    )

    # Add a ready command.
    @bot.event
    async def ready():
        """
        Called once when the bot goes online.
        """
        greeting = conf.get("greeting", GREETING)
        await bot._ws.send_privmsg(channel, greeting)
        log.info(nick, " is online")

    # Called on every message.
    @bot.event
    async def message(ctx):
        """
        Runs every time a message is sent in chat.
        """
        # make sure the bot ignores itself and the streamer
        if ctx.author.name.lower() == nick.lower():
            return

        # Log the message.
        log.debug(ctx.author.name, ": ", ctx.content)

        # Handle commands.
        await bot.handle_commands(ctx)

    return bot
