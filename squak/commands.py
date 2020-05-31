import asyncio
import logging

import vlc

log = logging.getLogger(__name__)


def add(commands, bot):
    """
    Add custom commands.
    """
    for command, path in commands.items():
        # Load the audio.
        track = vlc.MediaPlayer(path)

        # Define the command.
        @bot.command(name=command)
        async def play_track(ctx):
            # Play the track.
            log.info("Running command: %s", command)
            track.play()

            # Give the player time to load.
            await asyncio.sleep(1)

            # Wait for the rest of the track.
            await asyncio.sleep(track.get_length() / 1000 - 1)
