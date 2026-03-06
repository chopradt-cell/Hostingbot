import telebot
TOKEN = "8649446675:AAEqsrsDRkD9Jn1x0FgdjMA8N72Oz8qsSmk"
CHANNEL_ID = -1003655366573

bot = telebot.TeleBot("8649446675:AAEqsrsDRkD9Jn1x0FgdjMA8N72Oz8qsSmk")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Bot is Working!")

@bot.message_handler(content_types=['document'])
def handle_file(message):
    sent = bot.forward_message(
        CHANNEL_ID,
        message.chat.id,
        message.message_id
    )

    link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.message_id}"
    bot.reply_to(message, f"✅ File Stored!\n🔗 {link}")

bot.infinity_polling()
