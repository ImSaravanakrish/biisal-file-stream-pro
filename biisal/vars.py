# (c) adarsh-goel (c) @Useless07
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "TamilFɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/TamilMovies5K"
bisal_grp = "https://t.me/MovieDiscussion24x7"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20389440'))
    API_HASH = str(getenv('API_HASH', 'a1a06a18eb9153e9dbd447cfd5da2457'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6655526779:AAHkcPzBZDNtGYRfndozqEbocl1YqnyQVWE'))
    name = str(getenv('name', 'filetolink'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002062053288'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002062053288'))
    PORT = int(getenv('PORT', '8000'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "2063915639").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Yaarulanee'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://tamilbots.koyeb.app/".format(FQDN)
    else:
        URL = "https://tamilbots.koyeb.app/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'TamilMovies5K')) 
    UPDATES_GROUP = str(getenv('UPDATES_GROUP', 'MovieDiscussion24x7')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @Useless07 ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'tnshort.net')
    SHORTLINK_API = getenv('SHORTLINK_API', 'eb0d3ac51fe147d90318fd1a3b2a9446a57bdf96')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/rk_back_up/18')
