#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os
import re
from plugins.magnetic_link_regex import extract_info_hash_from_ml


def extract_link(text):
    custom_file_name = None
    url = None
    if "|" in text:
        url, custom_file_name = text.split("|")
        url = url.strip()
        custom_file_name = custom_file_name.strip()
    return url, custom_file_name
