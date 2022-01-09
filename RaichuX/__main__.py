from XRaichu.helpers.Calls.tgcalls import run
from pyrogram import idle
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



Bot.start() 
run() 
idle()
