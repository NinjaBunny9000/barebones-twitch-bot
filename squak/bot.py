import os
import logging
from twitchio.ext import commands

log = logging.getLogger(__name__)


def make(irc_token, client_id, nick, prefix, channel, greeting):
    """
    Create and return the bot.
    """
    bot = commands.Bot(
        irc_token=irc_token,
        client_id=client_id,
        nick=nick,
        prefix=prefix,
        initial_channels=[channel],
    )

    # Add a ready command.
    @bot.event
    async def ready():
        """
        Called once when the bot goes online.
        """
        await bot._ws.send_privmsg(channel, greeting)
        log.info(nick, " is online")

    return bot
