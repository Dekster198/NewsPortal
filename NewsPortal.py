import telebot
import feedparser
import random
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Я - новостной бот. Я умею работать со следующими источниками: Яндекс, Ведомости, МК, Лента. Для вызова списка команд введите /help')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Для информации о боте введите команду /info. Для выбора источника введите команду /source')
    elif message.text == '/source':
        message == 'Выберите источник'
        bot.register_next_step_handler(message, source(message))
    elif message.text == '/info':
        bot.send_message(message.from_user.id, 'Я - новостной бот. Я умею работать со следующими источниками: Яндекс, Ведомости, МК, Лента.')
    else:
        bot.send_message(message.from_user.id, 'Неизвестная команда. Введите /help')

news_auto_ya_keyb = types.InlineKeyboardMarkup()
news_auto_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_auto_ya')
news_auto_ya_keyb.add(news_auto_ya)
news_world_ya_keyb = types.InlineKeyboardMarkup()
news_world_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_world_ya')
news_world_ya_keyb.add(news_world_ya)
news_health_ya_keyb = types.InlineKeyboardMarkup()
news_health_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_health_ya')
news_health_ya_keyb.add(news_health_ya)
news_internet_ya_keyb = types.InlineKeyboardMarkup()
news_internet_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_internet_ya')
news_internet_ya_keyb.add(news_internet_ya)
news_science_ya_keyb = types.InlineKeyboardMarkup()
news_science_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_science_ya')
news_science_ya_keyb.add(news_science_ya)
news_politics_ya_keyb = types.InlineKeyboardMarkup()
news_politics_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_politics_ya')
news_politics_ya_keyb.add(news_politics_ya)
news_tech_ya_keyb = types.InlineKeyboardMarkup()
news_tech_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_tech_ya')
news_tech_ya_keyb.add(news_tech_ya)
news_eco_ya_keyb = types.InlineKeyboardMarkup()
news_eco_ya = types.InlineKeyboardButton(text='Показать новость', callback_data='news_eco_ya')
news_eco_ya_keyb.add(news_eco_ya)

news_auto_ved_keyb = types.InlineKeyboardMarkup()
news_auto_ved = types.InlineKeyboardButton(text='Показать новость', callback_data='news_auto_ved')
news_auto_ved_keyb.add(news_auto_ved)
news_internet_ved_keyb = types.InlineKeyboardMarkup()
news_internet_ved = types.InlineKeyboardButton(text='Показать новость', callback_data='news_internet_ved')
news_internet_ved_keyb.add(news_internet_ved)
news_politics_ved_keyb = types.InlineKeyboardMarkup()
news_politics_ved = types.InlineKeyboardButton(text='Показать новость', callback_data='news_politics_ved')
news_politics_ved_keyb.add(news_politics_ved)
news_tech_ved_keyb = types.InlineKeyboardMarkup()
news_tech_ved = types.InlineKeyboardButton(text='Показать новость', callback_data='news_tech_ved')
news_tech_ved_keyb.add(news_tech_ved)
news_eco_ved_keyb = types.InlineKeyboardMarkup()
news_eco_ved = types.InlineKeyboardButton(text='Показать новость', callback_data='news_eco_ved')
news_eco_ved_keyb.add(news_eco_ved)

news_cult_mk_keyb = types.InlineKeyboardMarkup()
news_cult_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_cult_mk')
news_cult_mk_keyb.add(news_cult_mk)
news_science_mk_keyb = types.InlineKeyboardMarkup()
news_science_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_science_mk')
news_science_mk_keyb.add(news_science_mk)
news_social_mk_keyb = types.InlineKeyboardMarkup()
news_social_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_social_mk')
news_social_mk_keyb.add(news_social_mk)
news_politics_mk_keyb = types.InlineKeyboardMarkup()
news_politics_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_politics_mk')
news_politics_mk_keyb.add(news_politics_mk)
news_incident_mk_keyb = types.InlineKeyboardMarkup()
news_incident_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_incident_mk')
news_incident_mk_keyb.add(news_incident_mk)
news_sport_mk_keyb = types.InlineKeyboardMarkup()
news_sport_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_sport_mk')
news_sport_mk_keyb.add(news_sport_mk)
news_eco_mk_keyb = types.InlineKeyboardMarkup()
news_eco_mk = types.InlineKeyboardButton(text='Показать новость', callback_data='news_eco_mk')
news_eco_mk_keyb.add(news_eco_mk)

news_world_lenta_keyb = types.InlineKeyboardMarkup()
news_world_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_world_lenta')
news_world_lenta_keyb.add(news_world_lenta)
news_media_lenta_keyb = types.InlineKeyboardMarkup()
news_media_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_media_lenta')
news_media_lenta_keyb.add(news_media_lenta)
news_cult_lenta_keyb = types.InlineKeyboardMarkup()
news_cult_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_cult_lenta')
news_cult_lenta_keyb.add(news_cult_lenta)
news_forces_lenta_keyb = types.InlineKeyboardMarkup()
news_forces_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_forces_lenta')
news_forces_lenta_keyb.add(news_forces_lenta)
news_sport_lenta_keyb = types.InlineKeyboardMarkup()
news_sport_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_sport_lenta')
news_sport_lenta_keyb.add(news_sport_lenta)
news_science_lenta_keyb = types.InlineKeyboardMarkup()
news_science_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_science_lenta')
news_science_lenta_keyb.add(news_science_lenta)
news_eco_lenta_keyb = types.InlineKeyboardMarkup()
news_eco_lenta = types.InlineKeyboardButton(text='Показать новость', callback_data='news_eco_lenta')
news_eco_lenta_keyb.add(news_eco_lenta)

def source(message):
    keyb_source = types.InlineKeyboardMarkup()
    key_yandex = types.InlineKeyboardButton(text='Яндекс', callback_data='yandex')
    keyb_source.add(key_yandex)
    key_vedomosti = types.InlineKeyboardButton(text='Ведомости', callback_data='vedomosti')
    keyb_source.add(key_vedomosti)
    key_mk = types.InlineKeyboardButton(text='МК', callback_data='mk')
    keyb_source.add(key_mk)
    key_lenta = types.InlineKeyboardButton(text='Лента', callback_data='lenta')
    keyb_source.add(key_lenta)
    bot.send_message(message.chat.id, text='Выберите источник', reply_markup=keyb_source)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yandex':
        ya_category = types.InlineKeyboardMarkup()
        key_auto = types.InlineKeyboardButton(text='Авто', callback_data='auto_ya')
        ya_category.add(key_auto)
        key_world = types.InlineKeyboardButton(text='В мире', callback_data='world_ya')
        ya_category.add(key_world)
        key_health = types.InlineKeyboardButton(text='Здоровье', callback_data='health_ya')
        ya_category.add(key_health)
        key_internet = types.InlineKeyboardButton(text='Интернет', callback_data='internet_ya')
        ya_category.add(key_internet)
        key_science = types.InlineKeyboardButton(text='Наука', callback_data='science_ya')
        ya_category.add(key_science)
        key_politics = types.InlineKeyboardButton(text='Политика', callback_data='politics_ya')
        ya_category.add(key_politics)
        key_tech = types.InlineKeyboardButton(text='Технологии', callback_data='tech_ya')
        ya_category.add(key_tech)
        key_eco = types.InlineKeyboardButton(text='Экономика', callback_data='eco_ya')
        ya_category.add(key_eco)
        bot.send_message(call.message.chat.id, text='Выберите категорию', reply_markup=ya_category)
    if call.data == 'auto_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/auto.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_auto_ya_keyb)
    if call.data == 'news_auto_ya':
        n = random.randint(2,19)
        NewsFeed = feedparser.parse('https://news.yandex.ru/auto.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_auto_ya_keyb)
    if call.data == 'world_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/world.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_world_ya_keyb)
    if call.data == 'news_world_ya':
        n = random.randint(2,20)
        NewsFeed = feedparser.parse('https://news.yandex.ru/world.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_world_ya_keyb)
    if call.data == 'health_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/health.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_health_ya_keyb)
    if call.data == 'news_health_ya':
        n = random.randint(2,19)
        NewsFeed = feedparser.parse('https://news.yandex.ru/health.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_health_ya_keyb)
    if call.data == 'internet_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/internet.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_internet_ya_keyb)
    if call.data == 'news_internet_ya':
        n = random.randint(2,8)
        NewsFeed = feedparser.parse('https://news.yandex.ru/internet.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_internet_ya_keyb)
    if call.data == 'science_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/science.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_science_ya_keyb)
    if call.data == 'news_science_ya':
        n = random.randint(2,13)
        NewsFeed = feedparser.parse('https://news.yandex.ru/science.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_science_ya_keyb)
    if call.data == 'politics_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/politics.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_politics_ya_keyb)
    if call.data == 'news_politics_ya':
        n = random.randint(2,20)
        NewsFeed = feedparser.parse('https://news.yandex.ru/politics.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_politics_ya_keyb)
    if call.data == 'tech_ya':
        n = random.randint(2,19)
        NewsFeed = feedparser.parse('https://news.yandex.ru/computers.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_tech_ya_keyb)
    if call.data == 'news_tech_ya':
        n = random.randint(2,19)
        NewsFeed = feedparser.parse('https://news.yandex.ru/computers.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_tech_ya_keyb)
    if call.data == 'eco_ya':
        NewsFeed = feedparser.parse('https://news.yandex.ru/business.rss')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_ya_keyb)
    if call.data == 'news_eco_ya':
        n = random.randint(2,11)
        NewsFeed = feedparser.parse('https://news.yandex.ru/business.rss')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_ya_keyb)
    if call.data == 'vedomosti':
        ved_category = types.InlineKeyboardMarkup()
        key_auto = types.InlineKeyboardButton(text='Авто', callback_data='auto_ved')
        ved_category.add(key_auto)
        key_internet = types.InlineKeyboardButton(text='Интернет', callback_data='internet_ved')
        ved_category.add(key_internet)
        key_politics = types.InlineKeyboardButton(text='Политика', callback_data='politics_ved')
        ved_category.add(key_politics)
        key_tech = types.InlineKeyboardButton(text='Технологии', callback_data='tech_ved')
        ved_category.add(key_tech)
        key_eco = types.InlineKeyboardButton(text='Экономика', callback_data='eco_ved')
        ved_category.add(key_eco)
        bot.send_message(call.message.chat.id, text='Выберите категорию', reply_markup=ved_category)
    if call.data == 'auto_ved':
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/auto')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_auto_ved_keyb)
    if call.data == 'news_auto_ved':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/auto')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_auto_ved_keyb)
    if call.data == 'internet_ved':
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/technology/internet')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_internet_ved_keyb)
    if call.data == 'news_internet_ved':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/technology/internet')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_internet_ved_keyb)
    if call.data == 'politics_ved':
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/politics')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_politics_ved_keyb)
    if call.data == 'news_politics_ved':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/politics')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_politics_ved_keyb)    
    if call.data == 'tech_ved':
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/technology')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_tech_ved_keyb)
    if call.data == 'news_tech_ved':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/technology')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_tech_ved_keyb)
    if call.data == 'eco_ved':
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/economics')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_ved_keyb)
    if call.data == 'news_eco_ved':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://www.vedomosti.ru/rss/rubric/economics')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_ved_keyb)
    if call.data == 'mk':
        mk_category = types.InlineKeyboardMarkup()
        mk_culture = types.InlineKeyboardButton(text='Культура', callback_data='mk_culture')
        mk_category.add(mk_culture)
        mk_science = types.InlineKeyboardButton(text='Наука', callback_data='mk_science')
        mk_category.add(mk_science)
        mk_social = types.InlineKeyboardButton(text='Общество', callback_data='mk_social')
        mk_category.add(mk_social)
        mk_politics = types.InlineKeyboardButton(text='Политика', callback_data='mk_politics')
        mk_category.add(mk_politics)
        mk_incident = types.InlineKeyboardButton(text='Происшествия', callback_data='mk_incident')
        mk_category.add(mk_incident)
        mk_sport = types.InlineKeyboardButton(text='Спорт', callback_data='mk_sport')
        mk_category.add(mk_sport)
        mk_eco = types.InlineKeyboardButton(text='Экономика', callback_data='mk_eco')
        mk_category.add(mk_eco)
        bot.send_message(call.message.chat.id, text='Выберите категорию', reply_markup=mk_category)
    if call.data == 'mk_culture':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/culture/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_cult_mk_keyb)
    if call.data == 'news_cult_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/culture/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_cult_mk_keyb)
    if call.data == 'mk_science':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/science/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_science_mk_keyb)
    if call.data == 'news_science_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/science/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_science_mk_keyb)
    if call.data == 'mk_social':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/social/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_social_mk_keyb)
    if call.data == 'news_social_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/social/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_social_mk_keyb)
    if call.data == 'mk_politics':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/politics/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_politics_mk_keyb)
    if call.data == 'news_politics_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/politics/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_politics_mk_keyb)
    if call.data == 'mk_incident':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/incident/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_incident_mk_keyb)
    if call.data == 'news_incident_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/incident/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_incident_mk_keyb)
    if call.data == 'mk_sport':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/sport/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_sport_mk_keyb)
    if call.data == 'news_sport_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/sport/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_sport_mk_keyb)
    if call.data == 'mk_eco':
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/economics/index.xml')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_mk_keyb)
    if call.data == 'news_eco_mk':
        n = random.randint(2,49)
        NewsFeed = feedparser.parse('https://www.mk.ru/rss/economics/index.xml')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_mk_keyb)
    if call.data == 'lenta':
        lenta_category = types.InlineKeyboardMarkup()
        lenta_world = types.InlineKeyboardButton(text='В мире', callback_data='lenta_world')
        lenta_category.add(lenta_world)
        lenta_media = types.InlineKeyboardButton(text='Интернет и СМИ', callback_data='lenta_media')
        lenta_category.add(lenta_media)
        lenta_culture = types.InlineKeyboardButton(text='Культура', callback_data='lenta_culture')
        lenta_category.add(lenta_culture)
        lenta_forces = types.InlineKeyboardButton(text='Силовые структуры', callback_data='lenta_forces')
        lenta_category.add(lenta_forces)
        lenta_sport = types.InlineKeyboardButton(text='Спорт', callback_data='lenta_sport')
        lenta_category.add(lenta_sport)
        lenta_science = types.InlineKeyboardButton(text='Наука и техника', callback_data='lenta_science')
        lenta_category.add(lenta_science)
        lenta_eco = types.InlineKeyboardButton(text='Экономика', callback_data='lenta_eco')
        lenta_category.add(lenta_eco)
        bot.send_message(call.message.chat.id, text='Выберите категорию', reply_markup=lenta_category)
    if call.data == 'lenta_world':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/world')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_world_lenta_keyb)
    if call.data == 'news_world_lenta':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/world')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_world_lenta_keyb)
    if call.data == 'lenta_media':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/media')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_media_lenta_keyb)
    if call.data == 'news_media_lenta':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/media')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_media_lenta_keyb)
    if call.data == 'lenta_culture':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/culture')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_cult_lenta_keyb)
    if call.data == 'news_cult_media':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/culture')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_cult_lenta_keyb)
    if call.data == 'lenta_forces':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/forces')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_forces_lenta_keyb)
    if call.data == 'news_forces_lenta':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/forces')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_forces_lenta_keyb)
    if call.data == 'lenta_sport':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/sport')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_sport_lenta_keyb)
    if call.data == 'news_sport_lenta':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/sport')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_sport_lenta_keyb)
    if call.data == 'lenta_science':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/science')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_science_lenta_keyb)
    if call.data == 'news_science_lenta':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/science')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_science_lenta_keyb)
    if call.data == 'lenta_eco':
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/economics')
        entry = NewsFeed.entries[1]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_eco_lenta_keyb)
    if call.data == 'news_eco_lenta':
        n = random.randint(2,199)
        NewsFeed = feedparser.parse('https://lenta.ru/rss/news/eco')
        entry = NewsFeed.entries[n]
        message_bot = (str(entry.title) + '\nСсылка: ' + str(entry.link))
        bot.send_message(call.message.chat.id, message_bot)
        bot.send_message(call.message.chat.id, text='Чтобы вывести ещё новость - нажмите', reply_markup=news_world_eco_keyb)

bot.polling(none_stop=True, interval=0)
