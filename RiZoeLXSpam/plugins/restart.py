import os
import sys
from RiZoeLXSpam import (Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, SUDO_USERS, DEV)
from .. import CMD_HNDLR as hl

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
async def restart(e):
   if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        text = "Restarting !!\n\n Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass
        try:
            await Riz11.disconnect()
        except Exception:
            pass
        try:
            await Riz12.disconnect()
        except Exception:
            pass
        try:
            await Riz13.disconnect()
        except Exception:
            pass
        try:
            await Riz14.disconnect()
        except Exception:
            pass
        try:
            await Riz15.disconnect()
        except Exception:
            pass
        try:
            await Riz16.disconnect()
        except Exception:
            pass
        try:
            await Riz17.disconnect()
        except Exception:
            pass
        try:
            await Riz18.disconnect()
        except Exception:
            pass
        try:
            await Riz19.disconnect()
        except Exception:
            pass
        try:
            await Riz20.disconnect()
        except Exception:
            pass
        try:
            await Riz21.disconnect()
        except Exception:
            pass
        try:
            await Riz22.disconnect()
        except Exception:
            pass
        try:
            await Riz23.disconnect()
        except Exception:
            pass
        try:
            await Riz24.disconnect()
        except Exception:
            pass
        try:
            await Riz25.disconnect()
        except Exception:
            pass
        try:
            await Riz26.disconnect()
        except Exception:
            pass
        try:
            await Riz27.disconnect()
        except Exception:
            pass
        try:
            await Riz28.disconnect()
        except Exception:
            pass
        try:
            await Riz29.disconnect()
        except Exception:
            pass
        try:
            await Riz30.disconnect()
        except Exception:
            pass
        try:
            await Riz31.disconnect()
        except Exception:
            pass
        try:
            await Riz32.disconnect()
        except Exception:
            pass
        try:
            await Riz33.disconnect()
        except Exception:
            pass
        try:
            await Riz34.disconnect()
        except Exception:
            pass
        try:
            await Riz35.disconnect()
        except Exception:
            pass
        try:
            await Riz36.disconnect()
        except Exception:
            pass
        try:
            await Riz37.disconnect()
        except Exception:
            pass
        try:
            await Riz38.disconnect()
        except Exception:
            pass
        try:
            await Riz39.disconnect()
        except Exception:
            pass
        try:
            await Riz40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
