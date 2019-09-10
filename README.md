[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y013678)

# Barebones Twitch Bot in Python

>**This README is a wip!**

This is a starter-kit for Twitch chat bot, if you wanna write one in Python. It utilizes the TwitchIO library and YAML files for storing secrets and config info.

It's pretty basic right now, but I'll be expanding on this in the near future. The larger, more complex Twitch bot is being developed [HERE](https://github.com/NinjaBunny9000/DeepThonk) during [Live-Streams on Twitch](https://twitch.tv/ninjabunny9000).


## Getting Started

Should be quick & easy to get up and running but, ofc, if you ever have questions about the specifics, please feel free to ask me during streams or post an issue above.

### Prerequisites
- [Python 3.6](https://www.python.org/downloads/release/python-368/)
- PIPENV -> `python -m pip install pipenv`
- oauth token & client-id for a Twitch account for your bot

### Installing
1. Clone the repo, unzip it somewhere
2. Open up a console window and navigate to the directory you unzipped it in
3. Install requirements with `pipenv install`
4. Copy & rename `integrations-example.yaml` to `integrations.yaml`
5. Pop in all your secrets into the respective areas in `integrations.yaml`
6. Back to the console, `pipenv run python bot.py` to start the bot
7. Type `!test` in the chatroom to test the bot's working

**You just installed a basic chat bot for Twitch!** Have fun expanding the bot with more commands!! :D

## Bot Interaction
Right now, you can only interact with the bot via the single command, `!test`. You can create similar commands pretty easily, just copy the function and change out the function name decorator arguement...

```python
@bot.command(name='likethis', aliases=['this'])
async def likethis(ctx):
    await ctx.send(f'Asuh, @{ctx.author.name}!')
```

Test is out with `!likethis` in chat! :D

## Events

There are 2 events that are used in the code right now.. `on_ready` and `on_event`.

### on_ready
This executes when the bot comes online, and will print out to the console. 
```python
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')
```

### event_message
This function executes once per event (or message) sent. You can make it handle input from chat that *aren't* necesarily commands, and fun stuff like that.

```python
@bot.event
async def event_message(message):
    print(message.content)
    await bot.handle_commands(message)
```

You can find more info in [TwitchIO's official documentation](https://twitchio.readthedocs.io/en/rewrite/twitchio.html).


## Progress & Development Info

### Contributors & Licenses

[NinjaBunny9000](https://github.com/NinjaBunny9000) - _Author, Project Manager_ - [Twitch](https://twitch.tv/ninjabunny9000) //  [Twitter](https://twitter.com/ninjabunny9000)

### Special Thanks
Literally everyone that's helped even the smallest bit during streams. Thank you so much, y'all!
