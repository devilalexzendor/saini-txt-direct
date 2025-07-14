#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22370423"))
API_HASH = environ.get("API_HASH", "026eada47b6991f2a9eec8461c7febb5")
BOT_TOKEN = environ.get("BOT_TOKEN", "7764014992:AAGoFWLmDtNQVUp_jCl872u5yfo0kb-nE40")

OWNER = int(environ.get("OWNER", "8150558323"))
CREDIT = environ.get("CREDIT", "𝐌𝐔𝐍𝐍𝐀𝐁𝐇𝐀𝐈𝐘𝐀 ❤️‍🔥")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
