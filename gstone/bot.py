import logging

from gstone.constants import GREETING
from gstone.constants import PREFIX
from twitchio.ext import commands

log = logging.getLogger(__name__)


def make(irc_token, client_id, channel, conf):
    """
    Create and return the bot.
    """
    bot = commands.Bot(
        irc_token=irc_token,
        client_id=client_id,
        nick=conf["nick"],
        prefix=conf.get("prefix", PREFIX),
        initial_channels=[channel],
    )

    # Add a ready command.
    @bot.event
    async def event_ready():
        """
        Called once when the bot goes online.
        """
        greeting = conf.get("greeting", GREETING)
        await bot._ws.send_privmsg(channel, greeting)
        log.info("%s is online", conf["nick"])

    # Called on every message.
    @bot.event
    async def event_message(ctx):
        """
        Runs every time a message is sent in chat.
        """
        # Handle commands.
        await bot.handle_commands(ctx)

    return bot
