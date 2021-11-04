# SuperBot
# made for SuperBot

import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from SuperBot.utils import admin_cmd, sudo_cmd
from SuperBot import ALIVE_NAME, Lastupdate
from . import sbdef
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sᥙρҽɾẞσ𝜏"

global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/63627b3e735af740f01f7.mp4"

""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await sbdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "**🌸🔥 sᴜᴘᴇʀʙᴏᴛ ᴀʟᴡᴀʏs ᴏɴ ғɪʀᴇ.. 🔥🌸**\n\n\n"
    pm_caption += "😎 ᴀʙᴏᴜᴛ sᴜᴘᴇʀʙᴏᴛ 😎\n\n"
    pm_caption += f"📍 **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ »»** `{version.__version__}`\n"
    pm_caption += "📍 **ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ »»** [ᴍᴜsᴛ ᴊᴏɪɴ ᴛʜɪs ᴄʜᴀɴɴᴇʟ](https://t.me/SuperBotOT)\n\n"
    pm_caption += "📍 **ᴄʀᴇᴀᴛᴏʀ »»** [ᴛᴇᴀᴍ sᴜᴘᴇʀʙᴏᴛ 😎](https://github.com/MadBoy-X/SuperBot)\n\n"
    pm_caption += f"📍 **ᴍʏ ᴏᴡɴᴇʀ 👑  »»** [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)
    
# SuperBot
# made for SuperBot by Jass
