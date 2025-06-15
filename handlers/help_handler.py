from telegram import Update
from telegram.ext import ContextTypes
from emerging_text import emerging_string

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    MESSAGE_HELP = '''🧭 Команды Скрытого Протокола:

/scan — анализ и сбор входящих данных
/decrypt — попытка расшифровки найденного артефакта
/path — прогноз возможных путей развития событий
/profile — досье на тебя
/update — внесение события в хронику
/echo — извлечение послания из временного вихря

⚠️ Внимание: доступ к командам может расширяться с ростом доверия Протокола.'''
    await emerging_string(update, context, MESSAGE_HELP)
