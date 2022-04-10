import os

import requests

from userbot import *
from userbot.utils import *


@flicks_cmd(pattern="paste( (.*)|$)")
async def _(event):
    xx = await edit_or_reply(event, "` 《 Pasting to nekobin... 》 `")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if not (input_str or event.is_reply):
        return await xx.edit("`Membalas Pesan/Dokumen atau Beri saya Beberapa Teks !`")
    if input_str:
        message = input_str
        downloaded_file_name = None
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                "./resources/downloads",
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            try:
                for m in m_list:
                    message += m.decode("UTF-8")
            except BaseException:
                message = "`Include long text / Reply to text file`"
            os.remove(downloaded_file_name)
        else:
            downloaded_file_name = None
            message = previous_message.message
    else:
        downloaded_file_name = None
        message = "`Include long text / Reply to text file`"
    if downloaded_file_name and downloaded_file_name.endswith(".py"):
        data = message
        key = (requests.post("https://nekobin.com/api/documents",
                             json={"content": data}) .json() .get("result") .get("key"))
    else:
        data = message
        key = (requests.post("https://nekobin.com/api/documents",
                             json={"content": data}) .json() .get("result") .get("key"))
    q = f"pasta-{key}"
    reply_text = f"• **Pasted to Nekobin :** [Neko](https://nekobin.com/{key})\n• **Raw Url :** : [Raw](https://nekobin.com/raw/{key})"
    try:
        ok = await bot.inline_query(BOT_USERNAME, q)
        await ok[0].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
        await xx.delete()
    except BaseException:
        await xx.edit(reply_text)


CMD_HELP.update(
    {
        "paste": f"**•Plugin :** `Paste`\
        \n\n  •  **•Perintah :** `{CMD_HANDLER}paste` <text/reply>\
        \n  •  **•Function : **Untuk Menyimpan text ke ke layanan Nekobin \
    "
    }
)
