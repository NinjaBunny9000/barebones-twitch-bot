import logging
import os
import pathlib
import sys

import click
import yaml
from dotenv import load_dotenv
from gstone import bot
from gstone import commands
from gstone.constants import LOG_LEVELS

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
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
        level=LOG_LEVELS[loglevel.lower()],
    )

    # Load the config.
    path = pathlib.Path(".") / ".env"
    load_dotenv(dotenv_path=path)
    conf = yaml.full_load(config)

    # Decode the config.
    irc_token = os.environ["SQUAK_TMI_TOKEN"]
    client_id = os.environ["SQUAK_CLIENT_ID"]

    # Setup the bot.
    gstonebot = bot.make(irc_token, client_id, channel, conf)
    commands.add(conf, gstonebot)

    # Run the bot.
    gstonebot.run()
