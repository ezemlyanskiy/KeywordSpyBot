import os

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
KEYWORDS = os.getenv('KEYWORDS', '').split(',')
USER_IDS_TO_NOTIFY = [int(uid.strip()) for uid in os.getenv('USER_IDS_TO_NOTIFY', '').split(',')]

print(f"Loaded BOT_TOKEN = {BOT_TOKEN[:10]}...")  # Masked for safety
print(f"KEYWORDS = {KEYWORDS}")
print(f"USER_IDS_TO_NOTIFY = {USER_IDS_TO_NOTIFY}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ You have subscribed to alerts!")

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    message_text = update.message.text.lower()

    if any(keyword in message_text for keyword in KEYWORDS):
        for user_id in USER_IDS_TO_NOTIFY:
            try:
                alert_text = f"🚨 Keyword alert from group:\n\n\"{update.message.text}\""
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
