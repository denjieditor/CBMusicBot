import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQGPeTAAoSBZE9dECVktyt8bRaRyIJ3MaWTPOclLsT263H3eclVDVLaMT9kJb2xloH2NfXQBmfGEpQRnLIHUftTgTUlYSmT_Kaur30uXbPnINGitt3Vm7NRtz2lD79Mnq6nXmIn_H_N8FApYy3TlMNrt3BofFc9ujb3kLMx3yvt2L_wnRA_yAnVkHxboAGx1ZaWp29AQVtzeFxNGhq82tiMx8lordxpUoTKsIAks-aGz3WEU6ezwSs1y2QLnZKhyZ3qOHUuB4_9c_GBEAWUM2oOPGz5LEO6L-w6y4oDVBc37hg11Ljp8SoLD37Vyf-VSX6G_L1AL_wTEO7odoob8tLixoH0oEwAAAAHMd5hzAQ")
BOT_TOKEN = getenv("7725357171:AAEM1T16TbfLJ0zYYBUNqPWLRBojDOdu_VU")
BOT_NAME = getenv("BOT_NAME", "🆁🅸🅺🅰乂𝓜𝓾𝓼𝓲𝓬🎵")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("26179888"))
API_HASH = getenv("b63b1c69cf3bcd032d4a2463cc84be2e")
BOT_USERNAME = getenv("BOT_USERNAME", "@Lonelyxmusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "🆁🅸🅺🅰乂Assistant🎵")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/animeclanzero2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/animeclan2")
OWNER_NAME = getenv("OWNER_NAME", "@denji_god) # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("5478596071")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://denji:@denji.0qi3h.mongodb.net/?retryWrites=true&w=majority&appName=denji") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
