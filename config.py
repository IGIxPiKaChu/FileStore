# ==========================================
# Krovik File Store Bot Config
# ==========================================
# Credits: @CodeFlix_Bots, @rohit_1888
# Your personal bot settings are below
# ==========================================

import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# ---------------- TELEGRAM BOT ----------------
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7462299639:AAHvIVZMP3jXQApQnz52fwDl2xbaUCjSNT0")
APP_ID = int(os.environ.get("APP_ID", "25165701"))  # Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2b64f26c1d8841d48b295f0db6e79639")  # Your API Hash

# ---------------- OWNER & CHANNEL ----------------
OWNER = os.environ.get("OWNER", "IGIxPiKaChu")  # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "5373224722"))  # Owner Telegram ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002380560765"))  # Your database channel ID

# ---------------- DATABASE ----------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://shainmeena950_db_user:71hH42ozcdMfaKRh@cluster0.j7vsvfq.mongodb.net/FileStoreDB?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "FileStoreDB")

# ---------------- BOT SETTINGS ----------------
PORT = os.environ.get("PORT", "8001")
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 = no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/CodeflixSupport")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @nova_flix</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# ---------------- MESSAGES ----------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> I am File Store Bot, I can store files in a private channel and share special links.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>Join our channels and click Reload to get your requested file.</b></blockquote>")

HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ᴜsᴇʀ ᴀssɪsᴛᴀɴᴛ ᴘʟᴜɢɪɴ.\nCommands:\n/start\n/about\n/help</blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/cosmic_freak>Yato</a>\n◈ Developer: <a href=https://t.me/cosmic_freak>subaru</a></blockquote></b>"

CMD_TXT = """<blockquote><b>» Admin Commands:</b></blockquote>
<b>›› /dlt_time :</b> set auto delete time
<b>›› /check_dlt_time :</b> check current delete time
<b>›› /dbroadcast :</b> broadcast document/video
<b>›› /ban :</b> ban a user
<b>›› /unban :</b> unban a user
<b>›› /banlist :</b> get list of banned users
<b>›› /addchnl :</b> add force sub channel
<b>›› /delchnl :</b> remove force sub channel
<b>›› /listchnl :</b> view added channels
<b>›› /fsub_mode :</b> toggle force sub mode
<b>›› /pbroadcast :</b> send photo to all users
<b>›› /add_admin :</b> add an admin
<b>›› /deladmin :</b> remove an admin
<b>›› /admins :</b> get list of admins
<b>›› /delreq :</b> remove leftover non-request users
"""

USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# ---------------- LOGGING ----------------
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# ---------------- MONGODB TEST ----------------
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

try:
    mongo_client = MongoClient(DB_URI, server_api=ServerApi('1'))
    mongo_client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
