import asyncio
import logging
from datetime import datetime

import vlc

log = logging.getLogger(__name__)


def get_tracks(conf):
    """
    Get a tracks dictionary from the conf.
    """
    return {name.lower(): path for name, path in conf["tracks"].items()}


def add_play(conf, bot):
    """
    Add the play command.
    """
    tracks = get_tracks(conf)

    # Track cooldown.
    last_play = None
    cooldown = conf.get("cooldown", 0)
    assert cooldown >= 0

    # Create the player.
    volume = conf.get("volume", 50)
    assert 0 <= volume <= 100
    player = vlc.MediaPlayer()
    player.audio_set_volume(volume)

    # Define the command.
    @bot.command(name="play")
    async def play(ctx):
        # Exit if playing.
        if player.is_playing():
            log.debug("a track is currently playing")
            return

        # Wait for cooldown.
        nonlocal last_play
        if last_play:
            delta = (datetime.now() - last_play).seconds
            if delta < cooldown:
                message = "still within cooldown (%ds < %ds)"
                log.debug(message, delta, cooldown)
                return

        # Get the track.
        track = " ".join(ctx.content.split(" ")[1:]).lower()

        try:
            # Get the path.
            path = tracks[track]
        except KeyError:
            log.debug("can't find track %s", track)
            return

        # Play the track.
        log.info("playing %s (%s)", track, path)
        player.set_mrl(path)
        player.play()
        last_play = datetime.now()

        # Give the player time to load and wait the full length.
        await asyncio.sleep(1)
        await asyncio.sleep(player.get_length() / 1000 - 1)

        # Reset the track.
        player.stop()


def add_list(conf, bot):
    """
    Add the list command.
    """
    tracks = get_tracks(conf)

    # Define the command.
    @bot.command(name="list")
    async def list(ctx):
        log.debug("listing tracks")
        await ctx.send(", ".join(tracks.keys()))


def add(conf, bot):
    """
    Add custom commands.
    """
    add_list(conf, bot)
    add_play(conf, bot)
