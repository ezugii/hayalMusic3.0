#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Özel Grup"
        logger_text = f"""
**Yeni Müzik Sorgusu**

**Sohbet:** {message.chat.title} [`{message.chat.id}`]
**Kullanıcı:** {message.from_user.mention}
**Kullanıcı Adı:** @{message.from_user.username}
**Kullanıcı Kimliği:** `{message.from_user.id}`
**Sohbet Linki:** {chatusername}

**Sorgu:** {message.text}

**Yayın Türü:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
