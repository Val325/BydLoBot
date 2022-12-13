import logging
import random
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


logging.basicConfig(
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
	level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text="Я быдло ёпта")

async def response(update: Update, context: ContextTypes.DEFAULT_TYPE):
        phrases = [
        "Лох, здоров",
        "Говно, это ты?",
        "Ты зырил извергона?",
        "Ты педик чтоль?",
        "Ебать копать"
                ]
        selectPhrase = random.randint(0, len(phrases) - 1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(phrases[selectPhrase]))

if __name__ == "__main__":
	application = ApplicationBuilder().token("5566909055:AAEwRJbzGB5H-VpVDz4KxV2agaS0Pa-pujA").build()

	strat_handler = CommandHandler("start", start)
	regular_msg = MessageHandler(filters.TEXT & (~filters.COMMAND), response)
	application.add_handler(strat_handler)
	application.add_handler(regular_msg)


	application.run_polling()

