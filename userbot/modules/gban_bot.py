"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.gban REASON
.ungban REASON"""
import asyncio
from userbot.utils import flicks_cmd
from userbot import ALIVE_NAME, G_BAN_LOGGER_GROUP, bot
# imported from uniborg by @heyworld

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@flicks_cmd(pattern="gbanb(?: |$)(.*)")
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("Set G_BAN_LOGGER_GROUP di vars jika tidak perintah tidak akan berfungsi!")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await bot.send_message(
            G_BAN_LOGGER_GROUP,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**gbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**Pengguna telah di gban oleh {DEFAULTUSER}**")
    asyncio.sleep(5)
    await event.delete()


@flicks_cmd(pattern="ungbanb(?: |$)(.*)")
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("Set G_BAN_LOGGER_GROUP di vars jika tidak perintah tidak akan berfungsi!")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await bot.send_message(
            G_BAN_LOGGER_GROUP,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**ungbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**Pengguna telah di ungban oleh {DEFAULTUSER}**")
    asyncio.sleep(5)
    await event.delete()
