# MEMELORD
A Discord bot that serves memes and random images from subreddits.

## Installation
1. Install the required packages by running `pip install -r requirements.txt`
2. Fill the config/config.py Configfile with your discord bot secret
```
__discord_token__ = 'YOUR_DISCORD_TOKEN_HERE'
__cooldown__ = 3
__activity__ = 'github.com/cybermyber/memelord'
__apiurl__ = 'https://meme-api.com/gimme/'
```
3. Run the bot by executing `python3 main.py`

## Usage
The bot has the following commands:
- `/meme` - sends a random meme
- `/random subreddit:<subreddit>` - sends a random image from the specified subreddit
- `/help` - shows an overview of the commands
- `/info` - shows an overview of used resources/projects

## Support
For support and assistance, join our Discord server at https://discord.gg/8BWxEBBV3Y

## Requirements
- py-cord
- aiohttp
- python>=3.9.0

## Many thanks to
- D3vd with Meme_Api https://github.com/D3vd/Meme_Api
- Pycord https://github.com/Pycord-Development/pycord

## Contribution
Feel free to contribute to this project by creating a pull request.
