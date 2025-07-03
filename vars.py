#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20708013"))
API_HASH = environ.get("API_HASH", "f0dbe59c7e43cc49fe9e83206ef9f828")
BOT_TOKEN = environ.get("8106410924:AAH2B_l2F-VuSYzL1O47j8QZ1AWln4_Bn_k", "")
OWNER = int(environ.get("OWNER", "1188631841"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '1188631841').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
