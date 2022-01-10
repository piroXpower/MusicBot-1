
from asyncio import QueueEmpty

from Image import tgcalls
from Image.queues import queues
from RaichuX import BOT_USERNAME, que
from RaichuX.helpers.Functions.admins import admins
from RaichuX.helpers.debug.channelmusic import get_chat_id
from RaichuX.helpers.debug.decorators import authorized_users_only, errors
from RaichuX.helpers.debug.filters import command, other_filters
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

ACTV_CALLS = []



# Back Button
BACK_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
)

# @Client.on_message(filters.text & ~filters.private)
# async def delcmd(_, message: Message):
#    if await delcmd_is_on(message.chat.id) and message.text.startswith("/") or message.text.startswith("!") or message.text.startswith("."):
#        await message.delete()
#    await message.continue_propagation()

# remove the ( # ) if you want the auto del cmd feature is on


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ Bot **reloaded correctly !**\n✅ **Admin list** has been **updated !**"
    )


@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in tgcalls.pytgcalls.active_calls:
        ACTV_CALLS(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await tgcalls.pytgcalls.pause_stream(chat_id)
        await message.reply_text(
            "⏸ **Track paused.**\n\n• **To resume the playback, use the**\n» /resume command."
        )


@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in tgcalls.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❌ **no music is paused**")
    else:
        await tgcalls.pytgcalls.resume_stream(chat_id)
        await message.reply_text(
            "▶️ **Track resumed.**\n\n• **To pause the playback, use the**\n» /pause command."
        )


@Client.on_message(command(["end", f"end@{BOT_USERNAME}", "stop", f"end@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in tgcalls.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❌ **no music is currently playing**")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await tgcalls.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("✅ **music playback has ended**")


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "next", f"next@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in tgcalls.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❌ **no music is currently playing**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await tgcalls.pytgcalls.leave_group_call(chat_id)
        else:
            await tgcalls.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        tgcalls.queues.get(chat_id)["file"],
                    ),
                ),
            )
                
    qeue = que.get(chat_id)
    if qeue:
        qeue.pop(0)
    if not qeue:
        return
    await message.reply_text("⏭ **You've skipped to the next song.**")
