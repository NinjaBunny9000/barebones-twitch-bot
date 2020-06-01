# Gossip Stone (gstone)

A Twitch bot that lets chat users play audio files in your stream.

## Installation

The easiest way to install and run the bot is via pipenv:

```
pip install --user pipenv
```

The bot uses libvlc to play sound files:

```
sudo apt install vlc
```

Use pipenv to install the bot and get a shell

```
pipenv install
pipenv shell
```

Now you should be able to run the bot:
```
gstone --help
```

## Configuration

There are two environment variables that you'll need to configure to set
up the bot. Toss them in a local .env file for convenience:

```
GSTONE_TMI_TOKEN=oauth:token
GSTONE_CLIENT_ID=id
```

These values are kept in a .env file so that they aren't leaked accidentally
on your stream. You can get an IRC token [here](https://twitchapps.com/tmi/)
and a client id [here](https://dev.twitch.tv/console/apps/create).

Next edit your `config.yaml`. The following lists all of the configuration
parameters with their default values:

```
nick: <your account name>
volume: 50 # 0 to 100
prefix: ! # the prefix for your commands
greeting: /me is ready to gossip # sent when you connect to chat
tracks:
  hey listen: listen.mp3
  thank you: thankyou.mp3
```

## Usage

Run the command with the path to the config followed by the name of the
twitch channel you want to connect to:

```
gstone config.yaml "rishiramraj"
```
