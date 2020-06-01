import asyncio
import logging
from datetime import datetime

import vlc

log = logging.getLogger(__name__)


def add_tracks(conf, bot):
    """
    Add track commands from the config.
    """
    # Decode the arguments.
    commands = conf["commands"]
    volume = conf.get("volume", 50)
    assert 0 <= volume <= 100
    cooldown = conf.get("cooldown", 0)
    assert cooldown >= 0

    # Track cooldown.
    last_play = None
    tracks = {}

    for command, path in commands.items():
        # Load the audio.
        tracks[command] = vlc.MediaPlayer(path)
        tracks[command].audio_set_volume(volume)

        # Define the command.
        @bot.command(name=command)
        async def play_track(ctx):
            log.info(" running %s (%s)", command, path)

            # Exit if playing.
            if tracks[command].is_playing():
                log.info(" %s is currently playing", path)
                return

            # Wait for cooldown.
            nonlocal last_play
            if last_play:
                delta = (datetime.now() - last_play).seconds
                if delta < cooldown:
                    message = " still within cooldown (%ds < %ds)"
                    log.info(message, delta, cooldown)
                    return

            # Play the track.
            tracks[command].play()
            last_play = datetime.now()

            # Give the player time to load and wait the full length.
            await asyncio.sleep(1)
            await asyncio.sleep(tracks[command].get_length() / 1000 - 1)

            # Reset the track.
            tracks[command].stop()


def add_list(conf, bot):
    """
    Add the list command.
    """
    lister = conf.get('list', 'list')
    commands = conf["commands"]
    assert lister not in commands

    # Define the command.
    @bot.command(name=lister)
    async def list_tracks(ctx):
        log.info(" running %s", lister)
        await ctx.send(', '.join(commands.keys()))


def add(conf, bot):
    """
    Add custom commands.
    """
    add_list(conf, bot)
    add_tracks(conf, bot)
