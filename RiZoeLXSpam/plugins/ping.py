#ping Pong

import os
import sys
from RiZoeLXSpam import (Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, SUDO_USERS, DEV)
from .. import CMD_HNDLR as hl
from telethon import events, version
from time import time
from datetime import datetime


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
async def ping(e):
   if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")  
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        pingop = f"⌾ ʀɪᴢᴏᴇʟ X sᴘᴀᴍ ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs"
        await fuk.edit(pingop)
