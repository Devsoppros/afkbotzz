
from os import getenv

# Get it from my.telegram.org
API_ID = getenv("8460373")
API_HASH = getenv("83d8e423197251216303abfcbed9e820")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("5846078236:AAE8-itHVHhgaXXpS1fFRpAMk4wpLbjUOYw")

# Database to save your chats and stats...
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lightyagami10:light@cluster0.zo6bf4g.mongodb.net/?retryWrites=true&w=majority")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
)  # Input type must be interger

# START IMAGE 
START_IMAGE = getenv("START_IMAGE", "")

# WELCOME IMAGE
WELCOME_IMAGE = getenv("WELCOME_IMAGE", "")
