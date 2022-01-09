import requests
from pyrogram import Client as Bot
from XRaichu.helpers.Calls.tgcalls import run
from pytgcalls import idle
from RaichuX import API_ID, API_HASH, BOT_TOKEN

with open("./Image/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="RaixhuX.modules"),
)



bot.start() 
run() 
idle()
