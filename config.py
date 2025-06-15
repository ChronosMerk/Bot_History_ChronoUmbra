import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    missing = []

    token_history_bot = os.getenv('TOKENTG')
    if not token_history_bot or len(token_history_bot) != 46:
        missing.append('TOKENTG')

    if missing:
        raise ValueError(f"❌ Отсутствуют переменные в .env: {', '.join(missing)}")
    return token_history_bot
