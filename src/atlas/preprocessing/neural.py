"""Minimal Unicode token boundaries; preserve Arabizi digits, negation and apostrophes."""

import re
import unicodedata

VERSION = "nfc-casefold-punctuation-v1"
TOKEN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*|[^\w\s]", re.UNICODE)


def normalize_text(text: str) -> str:
    return " ".join(TOKEN.findall(unicodedata.normalize("NFC", text).casefold()))
