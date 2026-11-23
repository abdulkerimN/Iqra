# 🌙 Iqra (اقرأ) — Islamic Telegram Bot

**Iqra** is a simple Islamic Telegram bot designed to share Quranic verses and authentic Hadith with users. It provides Arabic text, English translations, and source references to encourage learning, reflection, and daily remembrance of Allah.

## ✨ Features

- 📖 **Quranic Verses** — Discover verses from the Holy Quran.
- 📜 **Authentic Hadith** — Read Hadith with their source references.
- 🌙 **Daily Reminders** — Receive Islamic reminders and inspiration.
- 🔄 **Another Reminder** — Get another randomly selected verse or Hadith.
- 🇸🇦 **Arabic and English** — Read the original Arabic alongside its English meaning.
- 📚 **Source References** — Each entry includes its Quranic or Hadith reference.
- 💬 **Interactive Menu** — Navigate the bot using Telegram keyboard buttons.

## 🤖 Bot Commands

| Command | Description |
|---|---|
| `/start` | Start the bot and display the main menu |
| `/help` | Display available commands |
| `/tip` | Receive a Quranic verse or Hadith about knowledge |
| `/motivate` | Receive an Islamic reminder |

## 🛠️ Technologies Used

- Python
- python-telegram-bot
- python-dotenv
- Telegram Bot API

## 📁 Project Structure

```text
Iqra/
│
├── bot.py
├── messages.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Iqra.git
cd Iqra
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory:

```env
TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Get your bot token through [Telegram BotFather](https://t.me/BotFather).

**Important:** Never share your bot token or commit your `.env` file to GitHub.

### 6. Run the bot

```bash
python bot.py
```

Open your Telegram bot and send `/start`.

## 📚 Content Sources

Iqra shares Quranic verses and Hadith with their references.

- [Quran.com](https://quran.com/)
- [Sunnah.com](https://sunnah.com/)
- [Tanzil](https://tanzil.net/)

Translations and Hadith references should be checked against their original sources.

## 🚀 Future Improvements

- Daily scheduled Islamic reminders.
- Separate Quran and Hadith sections.
- Daily Dhikr collection.
- Favorite verses and Hadith.
- Customizable reminder schedules.
- Daily Islamic challenges.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find an issue or have an idea for improving Iqra, feel free to open an issue or submit a pull request.

## 📄 License

This project is open-source. A license can be added when the project licensing terms are decided.

---

**Iqra (اقرأ) — Read, Learn, Reflect, and Grow in Knowledge.** 🤍
