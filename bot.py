from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# এখানে তোমার নতুন bot token বসাও
BOT_TOKEN="8846846536:AAHjAXTsBghkLQ6veqA5tUDurSSoR3iI41E"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 Cartoon Thumbnail Bot এ স্বাগতম!\n\n"
        "ভিডিওর title পাঠাও, আমি thumbnail idea দিব 😎"
    )

async def make_thumbnail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    title = update.message.text

    thumb_text = f"🔥 {title[:20].upper()}!"
    
    idea = (
        f"🎭 Thumbnail Idea:\n"
        f"একটা funny cartoon character 😆\n"
        f"Bright background 🌈\n"
        f"Big text: {thumb_text}"
    )

    prompt = (
        f"Create a colorful YouTube cartoon thumbnail for '{title}', "
        f"funny cartoon character, bright colors, shocked face, "
        f"high quality, clickable style, big bold text."
    )

    reply = (
        f"✅ Thumbnail Ready!\n\n"
        f"📝 Thumbnail Text:\n{thumb_text}\n\n"
        f"{idea}\n\n"
        f"🤖 AI Image Prompt:\n{prompt}"
    )

    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, make_thumbnail))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
