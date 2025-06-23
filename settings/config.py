from dotenv import load_dotenv
import os

load_dotenv()  # aqui cargo la variables del .env

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
RULES_CHANNEL_ID = int(os.getenv("RULES_CHANNEL_ID"))
WELCOME_AUTO_ROLE_ID = int(os.getenv("WELCOME_AUTO_ROLE_ID"))

