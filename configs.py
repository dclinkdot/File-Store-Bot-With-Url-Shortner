import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23679347"))
  API_HASH = os.environ.get("API_HASH", "7de55f9c943538839c4bdb877724a773")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6616091482:AAHeCDgj1PD_20vHO6y27cFCtN83N_ERHLc")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@RadhaShyambot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001988500471"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "https://tnshort.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "9afa22b2c80ebd65dc44ac8047724ba17c650a5d")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5421323272"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://bhoomikbm9:XBxt4X2aH1msCHiU@cluster0.czv5bwi.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001924495958")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001873798465"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [DC](https://telegram.me/Movieshubdc) 
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Movieshubdc)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
