# Setname || setbio #

import os
from telethon.tl import functions
from RiZoeLXSpam import (Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, DEV)
from .. import CMD_HNDLR as hl
from telethon import events


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
async def name(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗡𝗔𝗠𝗘\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in DEV:
        names = e.text.split(" ", 1)
        RiZoeL = names[1]
        if len(e.text) > 5:
            firstname = RiZoeL
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#bio 
            
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗕𝗜𝗢\n\nCommand:\n\n.setbio <Message to change name of spam ids>"
    if e.sender_id in DEV:
        fukyou = e.text.split(" ", 1)
        message = fukyou[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
