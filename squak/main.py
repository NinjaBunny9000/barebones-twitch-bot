import click
import vlc
from time import sleep


@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path):
    # Play the clip.
    player = vlc.MediaPlayer(path)
    player.play()

    # Give the player time to load.
    sleep(1)

    # Wait for the residual.
    sleep(player.get_length()/1000 - 1)
