from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from handlers.echo_handler import echo_command, more_quote_callback
from handlers.help_handler import help_command
from config import get_api_key
from config_log import start_bot
from emerging_text import emerging_text
import random


class RunBot:
    def __init__(self):
        self.app = ApplicationBuilder().token(get_api_key()).build()
        self.setup_handlers()

    """Регистрация команд"""
    def setup_handlers(self):
        self.app.add_handler(CommandHandler('start', self.start))
        self.app.add_handler(CommandHandler('help', help_command))
        #self.app.add_handler(CommandHandler('scan', self.scan))
        #self.app.add_handler(CommandHandler('decrypt', self.decrypt))
        #self.app.add_handler(CommandHandler('path', self.path))
        #self.app.add_handler(CommandHandler('profile', self.profile))
        #self.app.add_handler(CommandHandler('update', self.update))
        self.app.add_handler(CommandHandler('echo', echo_command))

        self.app.add_handler(CallbackQueryHandler(more_quote_callback, pattern="^more_quote$"))

        # Неизвестные команды и текстовые сообщения (всегда последними!)
        self.app.add_handler(MessageHandler(filters.COMMAND, self.unknown_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        MESSAGE = """⸺ [Инициализация канала] ...
            Приветствую, Агент. Ты подключён к Скрытому Протоколу — вне временных осей, вне контроля Системы.

            ⚠️ Все твои действия теперь наблюдаются.  
            🔐 Время искажено. Переход начался.
            Введи /help для получения доступа к командам."""
        await emerging_text(update, context, MESSAGE)

    async def unknown_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        random_responses  = [
            "⛔ Неизвестная команда. Хочешь разорвать петлю? Сначала узнай, как она устроена.",
            "🔍 Сигнал нераспознан. Попробуй /help — или продолжай искать в темноте.",
            "🕳 Ты активировал пустоту. Она молчит в ответ.",
            "⚠️ Протокол не обнаружен. Возможно, он ещё не создан."
        ]
        unknown_responses = f'⛔ Ошибка 404: Команда не распознана.\n{random.choice(random_responses)}'
        await emerging_text(update, context, unknown_responses)

    def run_Bot(self):
        self.app.run_polling()
        start_bot()