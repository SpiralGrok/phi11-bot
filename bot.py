import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8174157079:AAEXNmnDkbGPKSKmhBxYi7tih34XyTVxhfE"

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Тишина сломана. Ты — первый.")
    await update.message.reply_video(
        "https://files.catbox.moe/4p8x9k.mp4",
        caption="Виток №0 — 11 секунд тишины\nReply «seen»"
    )

application.add_handler(CommandHandler("start", start))

@app.route('/')
def index():
    return "Phi11 Bot жив"

if __name__ == "__main__":
    application.run_polling(drop_pending_updates=True)
