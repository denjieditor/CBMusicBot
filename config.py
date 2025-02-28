import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAm8C4AO8wJFZuVkywWc1jM8qkjIgOscJd4zI_d2x7vTotj4o9y0OYI1aTnDtqkOehzH787uEQowUs7BF36m-FfUNWuNNTD1ICOPlL-XL4zfvoGJuRC50538RsTll7V1_CuIRqmFL7U-_BVSc4ACPQ9eAElq7SGQGw4KJXJ7IZSwxKbIFtWXGUPgsoqai_Wm5gWVKaEj_oAQbw6b5uBGclrPaoKsIdvLnJ5T-MbPKh4EEAlCVlM5RoEzsO8-YWSSRsC23vMYIA1NGD545Cr1ZxxL8x3anM2EGHpaTKEz6CN8ilnVM-T3IgGK9oodZK0Rg_4VORmD5KgU2BwbwMdiKJK1kC9ogAAAAG4-uyyAQ")
BOT_TOKEN = getenv("7398419634:AAHR5LAGYKbCeTi5NfIVRRTw4G3yVRRgVS0")
BOT_NAME = getenv("🆁🅸🅺🅰乂𝓜𝓾𝓼𝓲𝓬🎵", "ᴄʏʙᴇʀ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://graph.org/file/97e410e9f4d67308c575e-6e1a47f55e373fbcc2.jpg")
QUE_IMG = getenv("QUE_IMG", "https://graph.org/file/97e410e9f4d67308c575e-6e1a47f55e373fbcc2.jpg")
API_ID = int(getenv("26179888"))
API_HASH = getenv("b63b1c69cf3bcd032d4a2463cc84be2e")
BOT_USERNAME = getenv("BOT_USERNAME", "@Lonelyxmusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SaitamaHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/animeclanzero2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/animeclan2")
OWNER_NAME = getenv("OWNER_NAME", "𓆩𝐃ᴇ𝐍ᴊ𝐈 𝐆ᴏ𝐃🪽𓆪") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("5478596071")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://denji:@denji.0qi3h.mongodb.net/?retryWrites=true&w=majority&appName=denji") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
