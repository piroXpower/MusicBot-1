import os
from os import path
from typing import Callable
from asyncio.queues import QueueEmpty

import aiofiles
import aiohttp
import converter
import ffmpeg
import requests
from RaichuX.Function.admins import admins as a
from RaichuX.Calls import callsmusic
from RaichuX.Calls.tgcalls import client as USER
from RaichuX.Queues.queues import queues
from RaichuX import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    DURATION_LIMIT,
    GROUP_SUPPORT,
    THUMB_IMG,
    CMD_IMG,
    UPDATES_CHANNEL,
    que,
)
from Raichu.youtube import youtube
from helpers.debug.admins import get_administrators
from helpers.debug.channelmusic import get_chat_id
from helpers.debug.chattitle import CHAT_TITLE
from helpers.debug.decorators import authorized_users_only
from helpers.debug.filters import command, other_filters
from helpers.debug.gets import get_url, get_file_name
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

# plus

chat_id = None
DISABLED_GROUPS = []
useer = "NaN"
ACTV_CALLS = []
