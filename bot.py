# импорт библиотек
import telebot

from config import *
from telebot import types
from main import get_answer

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	sti = open('Assets/sticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Мне нужно задать вопрос")

	markup.add(item1)

	bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - {1.first_name}, бот для тех.поддержки, который отвечает на часто задаваемые вопросы пользователей, предоставляет решения проблем и направляет запросы к специалистам при необходимости.'.format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

# функция на ответ
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'Мне нужно задать вопрос':
            def process_reply(message):
                answer = get_answer(message.text)
                try:
                    if answer:
                        bot.send_message(message.chat.id, answer)
                    else:
                        bot.send_message(message.chat.id, 'На такой вопрос нет ответа, мы отправили вопрос специалисту')
                        #типа отправка вопроса специалисту
                except Exception as a:
                    print(repr(a))	
            bot.send_message(message.chat.id, 'Задайте ваш вопрос')
            bot.register_next_step_handler(message, process_reply)

        else:
            bot.send_message(message.chat.id, 'Извините, я не понял☹️')	

# запуск бота
bot.polling(none_stop=True)	
