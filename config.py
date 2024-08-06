import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 22802491))
API_HASH = getenv("71ea7abef3751bbd8bd51d3b27b6bf3f")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7258014552:AAH_9L9pMrJdfSlFu66L7IPAZwaK8sylQBY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "Nmongodb+srv://jekishwb:jekishwb@cluster0.tsytm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0one"l)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002192977004))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6935797014))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BAAZAR_X7")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Friendly_Chatting_FC")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFb8DsAcamdXTFurHecjrr3YEgDYQofGkTbIZGgGdLmqlk8l5qMBUqsjLEAH5Q5TZdy7yrvyRicKDKHLFnM75n2iYYFvpF-G597z0A8muC9ClVn8aRSfMVjhAVGc1BxivNaoYOG46xoab1-2lPBlcKOe2m3ATedfokVvxiOsHp0x1-NZkLoWYyLz2ex0yriiGDgcP4B3zE_VGY3UIQdo_G5RtBZeBUgf9mddlj3VI3VwKo7dXXFCcqEE_Wx4puSPb6H-3a11tba3RUFTEPdoNRNMIqRlprGdusoHFokCz4fpAsDW2HPtgxNDRiM1t1DICc-YEtR_hOJkB7GZUFhjwneHvRytgAAAAGdZ90WAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
STATS_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
STREAM_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
