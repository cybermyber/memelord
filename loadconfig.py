"""Loads the config file and sets the variables"""
import os

config_file = os.path.join('.', 'config', 'config.py')

if os.path.exists(config_file):
    try:
        from config.config import __discord_token__
    except ImportError as exc:
        raise ValueError('Discord token is missing in config.py') from exc
    try:
        from config.config import __cooldown__
    except ImportError:
        __cooldown__ = 3
    try:
        from config.config import __activity__
    except ImportError:
        __activity__ = 'github.com/cybermyber/memelord'
    try:
        from config.config import __apiurl__
    except ImportError:
        __apiurl__ = 'https://meme-api.com/gimme/'
else:
    raise FileNotFoundError('Config file not found')
