import telebot
import pyshorteners
import config
import random
from telebot import types


bot = telebot.TeleBot(config.token, parse_mode='html')

botim = '@SecretLinkBot'

short = pyshorteners.Shortener()


inline = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton('🇷🇺 RU', callback_data='ru')
btn2 = types.InlineKeyboardButton('🇺🇿 UZ', callback_data='uz')
btn3 = types.InlineKeyboardButton('🇬🇧 EN', callback_data='en')
inline.add(btn, btn2, btn3)


@bot.callback_query_handler(func=lambda call: True)
def inline_func(call):
    if call.data == 'ru':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, '🇷🇺 Русский язык выбран!')
        bot.send_message(call.message.chat.id, '⤵️ Отправьте мне любую ссылку.')
        bot.register_next_step_handler(call.message, link_ru)

    elif call.data == 'uz':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, '🇺🇿 Uzbek tili tanlandi!')
        bot.send_message(call.message.chat.id, '⤵️ Xohlagan linkigizni menga junating')
        bot.register_next_step_handler(call.message, link_uz)

    elif call.data == 'en':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, '🇬🇧 EN selected!')
        bot.send_message(call.message.chat.id, '⤵️ Now, Send me any link.')
        bot.register_next_step_handler(call.message, link_en)


@bot.message_handler(commands=['start'])
def welcme(message):
    bot.send_message(message.chat.id, 'Salom <b>{0}</b>.\nSizga maqul kelgan tilni tanlang:'.format(message.from_user.first_name), reply_markup=inline)


@bot.message_handler(content_types=['text'])
def link_en(message):
    links = ['https', 'http']

    try:
        if not message.text == links:
            short = pyshorteners.Shortener()
            biglink = message.text
            e = short.isgd.short(biglink)
            e2 = short.dagd.short(biglink)
            e3 = short.clckru.short(biglink)
            e4 = short.qpsru.short(biglink)
            e5 = short.tinyurl.short(biglink)

            link = [e, e2, e3, e4, e5]
            lin = (random.choice(link))

            bot.reply_to(message, '🔗 Short link: {0}\n\n<b>{1}</b>'.format(lin, botim), disable_web_page_preview=True)

    except:
        bot.send_message(message.chat.id, "⚠️ Ups, it's not link")


@bot.message_handler(content_types=['text'])
def link_ru(message):
    links2 = ['https', 'http']

    try:
        if not message.text == links2:
            short2 = pyshorteners.Shortener()
            biglink2 = message.text
            r = short2.isgd.short(biglink2)
            r2 = short2.dagd.short(biglink2)
            r3 = short2.clckru.short(biglink2)
            r4 = short2.qpsru.short(biglink2)
            r5 = short2.tinyurl.short(biglink2)

            link2 = [r, r2, r3, r4, r5]
            lin2 = (random.choice(link2))

            bot.reply_to(message, '🔗 Вот мини-ссылка: {0}\n\n<b>{1}</b>'.format(lin2, botim), disable_web_page_preview=True)

    except:
        bot.send_message(message.chat.id, "⚠️ Хмм... Что-то пошло не так")


@bot.message_handler(content_types=['text'])
def link_uz(message):
    links3 = ['https', 'http']

    try:
        if not message.text == links3:
            short3 = pyshorteners.Shortener()
            biglink3 = message.text
            u = short3.isgd.short(biglink3)
            u2 = short3.dagd.short(biglink3)
            u3 = short3.clckru.short(biglink3)
            u4 = short3.qpsru.short(biglink3)
            u5 = short3.tinyurl.short(biglink3)

            link3 = [u, u2, u3, u4, u5]
            lin3 = (random.choice(link3))

            bot.reply_to(message, '🔗 Mana qisqartrilgan link: {0}\n\n<b>{1}</b>'.format(lin3, botim), disable_web_page_preview=True)

    except:
        bot.send_message(message.chat.id, "⚠️ Serverda hatolik!")



bot.polling(none_stop=True)