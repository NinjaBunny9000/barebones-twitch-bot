import logging
import os
import sys
import pathlib

import click
import yaml
from dotenv import load_dotenv
from squak import bot
from squak import commands
from squak.constants import LOG_LEVELS

log = logging.getLogger(__name__)


@click.command()
@click.option(
    "-ll",
    "--loglevel",
    default="info",
    help="The log level.",
    type=click.Choice(LOG_LEVELS.keys(), case_sensitive=False),
)
@click.argument("config", type=click.File("r"))
@click.argument("channel")
def main(channel, config, loglevel):
    """
    A bot that lets chat users play audio files in your stream.
    """
    # Setup logging.
    logging.basicConfig(stream=sys.stderr, level=LOG_LEVELS[loglevel.lower()])

    # Load the config.
    path = pathlib.Path('.') / '.env'
    load_dotenv(dotenv_path=path)
    conf = yaml.full_load(config)
    irc_token = os.environ["SQUAK_TMI_TOKEN"]
    client_id = os.environ["SQUAK_CLIENT_ID"]

    # Setup the bot.
    squakbot = bot.make(irc_token, client_id, channel, conf)
    commands.add(conf["commands"], squakbot)

    # Run the bot.
    squakbot.run()
