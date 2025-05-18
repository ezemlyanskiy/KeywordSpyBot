# KeywordSpyBot 🤖

**KeywordSpyBot** is a Telegram bot that monitors group messages and alerts specific users via private message when certain keywords are detected.

---

## 🚀 Features

- 📡 Monitors all incoming messages in a Telegram group
- 🔍 Scans messages for custom keywords (like `urgent`, `alert`, etc.)
- 📬 Sends private alerts to specified users
- 🔐 Uses `.env` file for clean, secure configuration
- ✅ Supports multiple keywords and recipients

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/ezemlyanskiy/KeywordSpyBot.git
   cd KeywordSpyBot
   ```

2. Create and activate a virtual environment
   ```bash
    python -m venv venv
    venv\Scripts\activate  # on Windows
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the root directory
    ```bash
    BOT_TOKEN=your_telegram_bot_token
    KEYWORDS=urgent,alert,check this
    USER_IDS_TO_NOTIFY=123456789,987654321
    ```

5. Start the bot
    ```bash
    python bot.py
    ```

## 📌 Important Notes

* Users must **start the bot in private chat** at least once to receive private alerts.
* The bot must be:
    * An **admin** in the group **OR**
    * Have **group privacy mode disabled** via @BotFather
