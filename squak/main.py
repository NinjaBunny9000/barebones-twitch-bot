import os
import click
import logging
import sys
from squak import bot
from dotenv import load_dotenv
from squak.constants import LOG_LEVELS

log = logging.getLogger(__name__)


@click.command()
@click.option(
    "-g", "--greeting", default="/me has landed!", help="The target channel.",
)
@click.option(
    "-c", "--channel", required=True, help="The target channel.",
)
@click.option(
    "-p", "--prefix", default="bot", help="The bots prefix.",
)
@click.option(
    "-n", "--nick", default="squaker", help="The bots nick.",
)
@click.option(
    "-ll",
    "--loglevel",
    default="info",
    help="The log level.",
    type=click.Choice(LOG_LEVELS.keys(), case_sensitive=False),
)
def main(loglevel, nick, prefix, channel, greeting):
    """
    Called to run the bot.
    """
    # Setup logging.
    logging.basicConfig(stream=sys.stderr, level=LOG_LEVELS[loglevel.lower()])

    # Get config.
    load_dotenv()
    irc_token = os.environ["SQUAK_TMI_TOKEN"]
    client_id = os.environ["SQUAK_CLIENT_ID"]

    # Setup the bot.
    squakbot = bot.make(irc_token, client_id, nick, prefix, channel, greeting)

    # Run the bot.
    # squakbot.run()
    print("hi")
