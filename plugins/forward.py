#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 


from pyrogram import filters
from pyrogram import Client as ace
from pyrogram.types import Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import time
import os
import json


@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("ace", prefixes=prefixes)
)
async def forward(bot: ace, m: Message):
    msg = await bot.ask(m.chat.id, "**Forward any message from the Target channel\nBot should be admin at both the Channels**")
    t_chat = msg.forward_from_chat.id
    msg1 = await bot.ask(m.chat.id, "**Send Starting Message From Where you want to Start forwarding**")
    msg2 = await bot.ask(m.chat.id, "**Send Ending Message from the same chat**")

    i_chat = msg1.forward_from_chat.id
    s_msg = int(msg1.forward_from_message_id)
    f_msg = int(msg2.forward_from_message_id) + 1
    chat_name = msg1.forward_from_chat.username  # Get the chat username (assuming it's available)

    await m.reply_text('**Forwarding Started**\n\nPress /restart to Stop and /log to get log TXT file')

    forwarded_messages = []  # Create an empty list to store forwarded messages

    try:
        for i in range(s_msg, f_msg):
            try:
                forwarded_message = await bot.copy_message(
                    chat_id=t_chat,
                    from_chat_id=i_chat,
                    message_id=i
                )
                forwarded_messages.append(forwarded_message.json())  # Serialize and append to the list
                time.sleep(2)
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))

    # Save the list of forwarded messages as a JSON file
    if chat_name:
        filename = f"{chat_name}docs.json"
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(forwarded_messages, json_file, ensure_ascii=False, indent=4)

        # Send the JSON file to the user
        await m.reply_document(document=filename, caption="Here is the JSON file with forwarded messages.")

    await m.reply_text("Done Forwarding")