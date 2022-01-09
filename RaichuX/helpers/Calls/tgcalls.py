from RaichuX.helpers.Queues import queues
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from RaichuX import API_HASH, API_ID, SESSION_NAME


Assistant = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(Assistant)


@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
        await Assistant.send_message(chat_id,"<b>•Music PlayBack Ended\n•Assistant Leaving This Group\n•Thanks For Using This Bot\n•Powered By:- @XRaichu_Official</b>") 
        await Assistant.leave_chat(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id, 
            InputStream(
                InputAudioStream(
                    queues.get(chat_id)["file"],
                ),
            ),
        )


run = pytgcalls.start
