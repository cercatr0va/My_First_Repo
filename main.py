import telebot
import datetime
import time
import threading
import random

# Токен нашего бота
bot = telebot.TeleBot('...')

# Файл с цитатами
CIT_FILE = '../../../PycharmProjects/ZeroCoder_1/quotes.txt'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, text='Привет! Я чат-бот, который будет отправлять тебе мудрые цитаты!')
    # Запуск потока для отправки цитат в нужное время
    reminder_thread = threading.Thread(target=send_cit, args=(message.chat.id,))
    reminder_thread.start()


def load_quotes():
    """Загружает цитаты из файла и возвращает список."""
    try:
        with open(CIT_FILE, 'r', encoding='utf-8') as file:
            quotes = file.readlines()
            quotes = [quote.strip() for quote in quotes if quote.strip()]  # Убираем пустые строки
            return quotes
    except FileNotFoundError:
        return ["Цитаты не найдены. Убедитесь, что файл quotes.txt существует."]


def send_cit(chat_id):
    """Отправляет случайную цитату в определённое время."""
    # Время отправки цитат
    first_cit = "18:40"
    second_cit = "18:42"
    third_cit = "18:44"

    quotes = load_quotes()  # Загружаем цитаты из файла
    if not quotes:
        bot.send_message(chat_id, text="Не удалось загрузить цитаты.")
        return

    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_cit or now == second_cit or now == third_cit:
            # Выбираем случайную цитату из списка
            random_quote = random.choice(quotes)
            bot.send_message(chat_id, text=random_quote)
            time.sleep(61)  # Чтобы избежать повторной отправки в ту же минуту
        time.sleep(1)


bot.polling(none_stop=True)
