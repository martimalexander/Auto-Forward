#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5796451094:AAFHHF9FsomhKCIu8uOY-UX8YGvN79-yYLY")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID","9907811"))
    API_HASH = os.environ.get("API_HASH","b5adb7f7d4a096750edec1bc6daacd56")
    AUTH_USERS = os.environ.get("OWNER","5149523544")