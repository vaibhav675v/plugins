# RiZoeL X Spam | © 2022-2023 @RiZoeLX
# Kang With Credits


from RiZoeLXSpam import (Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, DEV, SUDO_USERS, hl, RiZoeL)
import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect


def load_plugins(shortname):
        path = Path(f"RiZoeLXSpam/plugins/{shortname}.py")
        name = "RiZoeLXSpam.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.logger = logging.getLogger(shortname)
        # support for paperplaneextended
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["RiZoeLXSpam.plugins." + shortname] = mod
        print("• RiZoeLXspam Successfully imported:  " + shortname)


async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)



def Start_Assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/{shortname}.py")
        name = "RiZoeLXSpam.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Checking Bot Token......")
        print("Starting Bot")
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/{shortname}.py")
        name = "RiZoeLXSpam.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.modules["RiZoeLXSpam.assistant" + shortname] = mod


def load_Assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/plugins/{shortname}.py")
        name = "RiZoeLXSpam.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("> Loading Spam Assistant <")
        print("XSpam Assistant " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/plugins/{shortname}.py")
        name = "RiZoeLXSpam.assistant.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.modules["RiZoeLXSpam.assistant.plugins." + shortname] = mod
        print("XSpam Assistant  " + shortname)
