from telegram import Update
from telegram.ext import ContextTypes
import asyncio

async def emerging_text(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    message: str,
    speed: float = 0.03,
    animation_cycles: int = 3,
    animation_delay: float = 0.4
):
    chat_id = update.effective_chat.id

    # Отправляем начальное сообщение
    sent_message = await context.bot.send_message(chat_id=chat_id, text="⸺ [Инициализация]")

    await animal_text(animation_cycles, sent_message, animation_delay)

    # После анимации — "печатаем" основное сообщение
    if 'Ошибка' in message:
        text_so_far = ""
    else:
        text_so_far = "⸺"

    for char in message[0:]:
        text_so_far += char
        await asyncio.sleep(speed)
        try:
            await sent_message.edit_text(text_so_far)
        except:
            pass


async def emerging_string(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    message: str,
    animation_delay: float = 0.7
):
    lines = message.strip().split('\n')
    chat_id = update.effective_chat.id

    # Отправляем начальное сообщение
    sent_message = await context.bot.send_message(chat_id=chat_id, text="⸺ [Инициализация справки]")

    # Постепенно добавляем строки и редактируем
    text_so_far = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        text_so_far += line + "\n"
        await asyncio.sleep(animation_delay)
        try:
            await sent_message.edit_text(text_so_far.strip())
        except Exception as e:
            print(f"Ошибка редактирования: {e}")


# Загрузочная анимация: [.] [..] [...] и т.д.
async def animal_text(animation_cycles, sent_message, animation_delay):
    dots = ["[.]", "[..]", "[...]"]
    for _ in range(animation_cycles):
        for dot in dots:
            try:
                await sent_message.edit_text(f"⸺ {dot}")
            except:
                pass
            await asyncio.sleep(animation_delay)