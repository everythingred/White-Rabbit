# Built-in
import json
from os import environ
from pathlib import Path
# 3rd-party
from dotenv import dotenv_values

# White-Rabbit/src/localization.py
WHITE_RABBIT_DIR = Path(__file__).parent.parent

# Localization
DEFAULT_LOCALIZATION = "en"
LOCALIZATION_DIR = WHITE_RABBIT_DIR / "localization"

LOCALIZATIONS = {
    "en": "english.json",
    "fr": "french.json",
}

try:
    language_key = environ.get("LANGUAGE") or dotenv_values(".env")["LANGUAGE"]
except KeyError:
    language_key = DEFAULT_LOCALIZATION

localization_file = LOCALIZATION_DIR / LOCALIZATIONS[language_key]

LOCALIZATION_DATA = None
with open(localization_file, encoding='utf-8') as f:
    LOCALIZATION_DATA = json.load(f)
