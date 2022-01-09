import requests
from pyrogram import Client as Bot
from RaichuX.helpers.Calls.tgcalls import run
from pytgcalls import idle
from RaichuX import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./Image/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="RaichuX.modules"),
)



bot.start() 
run() 
idle()
