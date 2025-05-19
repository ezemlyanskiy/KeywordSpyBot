import os

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
USER_IDS_TO_NOTIFY = [int(uid.strip()) for uid in os.getenv('USER_IDS_TO_NOTIFY', '').split(',')]

if BOT_TOKEN is None:
    raise ValueError('BOT_TOKEN must be set')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Вы подписаны на уведомления о состоянии контейнера!")

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    message_text = update.message.text.lower()

    if "containerkilled" in message_text:
        if "alerts firing" in message_text:
            alert_text = "Упал контейнер системы, обрати внимание и проверь интеграции, подробности в чате мониторинга."
        elif "alerts resolved" in message_text:
            alert_text = "Контейнер системы поднялся, подробности в чате мониторинга."
        else:
            return

        for user_id in USER_IDS_TO_NOTIFY:
            try:
                await context.bot.send_message(chat_id=user_id, text=alert_text)
            except Exception as e:
                print(f"Failed to send message to {user_id}: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))

    print("🤖 Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
