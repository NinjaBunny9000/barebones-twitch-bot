import click
import logging
import sys
from squak.constants import LOG_LEVELS

log = logging.getLogger(__name__)


@click.command()
@click.option(
    "-ll",
    "--loglevel",
    default="warning",
    help="The log level.",
    type=click.Choice(LOG_LEVELS.keys(), case_sensitive=False),
)
def main(loglevel):
    """
    Called to run the bot.
    """
    # Setup logging.
    logging.basicConfig(stream=sys.stderr, level=LOG_LEVELS[loglevel.lower()])
