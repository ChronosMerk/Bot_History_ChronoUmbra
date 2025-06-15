from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from quotes import get_random_quote

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = get_random_quote()
    keyboard = [[InlineKeyboardButton("⚡️ Ещё цитату", callback_data="more_quote")]]
    await update.message.reply_text(
        f"[ЭХО ИЗ БУДУЩЕГО]\n[Поток открыт] ...\n{quote}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def more_quote_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = get_random_quote()
    await update.callback_query.edit_message_text(
        f"[ЭХО ИЗ БУДУЩЕГО]\n[Поток обновлён] ...\n{quote}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⚡️ Ещё цитату", callback_data="more_quote")]]
        )
    )
    await update.callback_query.answer()
