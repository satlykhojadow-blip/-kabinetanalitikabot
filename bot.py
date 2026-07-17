import telebot

TOKEN = "8824642174:AAFF84pSEyq3Qly8AQMIZcgTnGxeeUKHqac"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я работаю!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
