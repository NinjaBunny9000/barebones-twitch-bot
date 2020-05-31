import click
import vlc
from time import sleep


@bot.event
async def event_message(ctx):
    "Runs every time a message is sent in chat."

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ["BOT_NICK"].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if "hello" in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")


@click.command()
@click.argument("path", type=click.Path(exists=True))
def main(path):
    # Play the clip.
    player = vlc.MediaPlayer(path)
    player.play()

    # Give the player time to load.
    sleep(1)

    # Wait for the residual.
    sleep(player.get_length() / 1000 - 1)
