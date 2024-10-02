1import telebot
import requests

def get_usd_to_rub():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['RUB']
    else:
        return "Ошибка: Не удалось получить данные"



Telegram_token="BOT_TOKEN"
bot = telebot.TeleBot(Telegram_token)


name="Пользователь"
name_comand=["Сменить имя", "Поменять имя", "rename"]
# Определяем обработчик сообщений
otvet_na_start=("Здравтвуйте данный бот подскажет вам курс доллара\n Вы можете просто нас об этом спросить в свободной форме\nТакже с помощью команд: Поменять имя или rename вы можете сменить свой никнейм\n Благодарим что выбрали нас")
@bot.message_handler(func=lambda message: message.text == "/start")
def greet_user(message):
    # Отправляем пользователю приветственное сообщение
    bot.reply_to(message, otvet_na_start)
    bot.reply_to(message, "Введите ваше имя:")

flag=True
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global name
    global flag
    if flag:
        name=message.text
        flag=False
        bot.reply_to(message, "Ваше имя успешно добавлено, введите ваш запрос\n(например: какой сейчас курс)")
    # Отправляем пользователю ответное сообщение
    elif name_comand.count(message.text)>0:
        bot.reply_to(message, "Введите ваше имя:")
        flag=True
    else:
        bot.reply_to(message, f"{name} курс доллара на данный момент {get_usd_to_rub()}")

# Запускаем бота
bot.polling()