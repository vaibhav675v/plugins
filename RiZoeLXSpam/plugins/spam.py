# Spam || Bigspam || Delayspam #

import asyncio
import re
import os
from telethon import events
from telethon import functions, types
from RiZoeLXSpam import (Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, SUDO_USERS, DEV)
from .. import CMD_HNDLR as hl

Error = "@TheRiZoeL|@TheVenomxd|RiZoeL"

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}spam <count> <message to spam>\n\n{hl}spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            if re.search(Error.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On Owner")
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(Error.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On Owner")
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

Riz.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
async def bigspam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}bigspam <count> <message to spam>\n\n{hl}bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            if re.search(Error.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On owner")
            counter = int(rizoel[0])
            for _ in range(counter):
                if e.reply_to_msg_id:
                    await smex.reply(message)
                else:
                    await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            for _ in range(counter):
               smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
               await gifspam(e, smex) 
               await asyncio.sleep(0.4)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(Error.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On owner")
            counter = int(rizoel[0])
            for _ in range(counter):
               await e.client.send_message(e.chat_id, message)
               await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
async def delayspam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}delayspam <sleep time> <count> <message to spam>\n\n{hl}delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Rizoelsexy = Rizoel[1:]
        if len(Rizoelsexy) == 2:
            message = str(Rizoelsexy[1])
            if re.search(Error.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On owner")
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                if e.reply_to_msg_id:
                    await smex.reply(message)
                else:
                    await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(Error.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On owner")
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                 await e.client.send_message(e.chat_id, message)
                 await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
