import telebot
from telebot import types

bot = telebot.TeleBot("5486817124:AAHKHtJK4nfaysN9pb1-ZuSuZVFJ48btk00")

@bot.message_handler(commands=['start', 'admin'])
def commands_messages(message):

    # start

    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Про нас', 'Анонси')
        markup.row('ISLND Shop', 'Допомога ЗСУ')
        bot.send_message(message.chat.id,
                         'Доброго дня! У цьому боті ви зможете отримати інформацію про телеканал Ісландія',
                         reply_markup = markup)

    # start end

    # admin panel

    elif message.text == '/admin':
        tempID = str(message.from_user.id)
        way = '/users/' + tempID
        try:
            with open(way, 'r') as f:
                data = f.read().splitlines()
            #print(data)
            if data[3] == 'admin':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.row('Список користувачів', "Замовлення")
                markup.row('Редагування функцій', "< Повернутися на початок")
                bot.send_message(message.chat.id,
                                 'Доброго дня! Що ви бажаєте зробити?',
                                 reply_markup = markup)
            else:
                bot.send_message(message.chat.id, 'Ви не адміністратор.')
        except:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            button_phone = types.KeyboardButton(text="Відправити номер телефону", request_contact=True)
            button_menu = types.KeyboardButton(text="< Повернутися на початок")
            keyboard.add(button_phone, button_menu)
            bot.send_message(message.chat.id,
                             "Для доступу до цієї функції, треба поділитись контактом.",
                             reply_markup=keyboard)

    # admin panel end

@bot.message_handler(func=lambda message: True)
def answer(message):
    if message.text == 'Про нас':
        bot.send_message(message.chat.id, 'Ісландія — український телеканал. Ми вчимо медіаграмотності, допомагаємо протистояти маніпуляціям і розпізнавати фейки. Ми маємо фахівців, досвід та розуміння необхідних процесів для ведення контрпропаганди.\n\nНаші глядачі — спільнота людей, що зацікавлені в інтелектуальному та творчому розвитку як України та українців, так і у власному теж. Тому велику увагу ми також приділяємо культурним та медичним проєктам.')

    elif message.text == 'Анонси':
        bot.send_message(message.chat.id, "21:00\nНаживо\n\nhttps://youtu.be/R7t6c7_KOtc")

    elif message.text == 'ISLND Shop':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.row('Асортимент', 'Створити замовлення')
        markup.row('< Повернутися на початок')
        bot.send_message(message.chat.id,
                         'Що вас цікавить?',
                         reply_markup=markup)

    elif message.text == 'Асортимент':
        markup = types.InlineKeyboardMarkup(row_width=1)
        other = types.InlineKeyboardButton('>', callback_data='other1')
        markup.add(other)
        bot.send_photo(message.chat.id, "AgACAgIAAxkBAANZY1Z1o5w44LX2Jks_aeSe_pP9y5wAAvq8MRvogrhKwwXO5wchFKIBAAMCAAN5AAMqBA", "***Чашка Ріж русню***\n\nКолір: Чорний\nЦіна: 300 грн (при замовленні від 2 чашок ціна 250грн або комплект футболка + чашка = 850грн)", reply_markup=markup, parse_mode="Markdown")

        #bot.send_message(message.from_user.id, "Які саме реквізити оплати вам потрібні? 🤔", reply_markup=markup)

    elif message.text == 'Допомога ЗСУ':
        bot.send_message(message.chat.id, "Підтримати ЗСУ можна надіславши грогі на на нашу картка monobank ➜```5358 3853 5000 1550```", parse_mode="Markdown")

    elif message.text == '< Повернутися на початок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Про нас', 'Анонси')
        markup.row('ISLND Shop', 'Допомога ЗСУ')
        bot.send_message(message.chat.id,
                         'Повертаємося...',
                         reply_markup=markup)

    elif message.text == 'Створити замовлення':
        tempID = str(message.from_user.id)
        way = '/users/' + tempID
        try:
            with open(way, 'r') as f:
                data = f.read().splitlines()
            if data[3] == 'admin' or 'user':
                bot.send_message(message.chat.id, "Будь ласка, напишіть ПІБ на яке буде оформлюватись замовлення.")
                bot.register_next_step_handler(message, order_name)
        except:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            button_phone = types.KeyboardButton(text="Відправити номер телефону", request_contact=True)
            button_menu = types.KeyboardButton(text="< Повернутися на початок")
            keyboard.add(button_phone, button_menu)
            bot.send_message(message.chat.id,
                             "Для доступу до цієї функції, треба поділитись контактом.",
                             reply_markup=keyboard)


def reg_end(message):
    tempID = str(message.from_user.id)
    way = '/users/' + tempID
    file = open(way, 'a')
    file.write('\n' + message.text)
    file.close()

# order

def order_name(message):
    #print(message.text)
    tempID = str(message.from_user.id)
    way = '/orders/' + tempID
    file = open(way, 'w')
    name = str(message.text)
    file.write("ПІБ: " + name)
    file.close()
    bot.send_message(message.chat.id, "Напишіть контактний телефон")
    bot.register_next_step_handler(message, order_phone)

def order_phone(message):
    #print(message.text)
    tempID = str(message.from_user.id)
    way = '/orders/' + tempID
    file = open(way, 'a')
    name = str(message.text)
    file.write("\nКонтактний телефон: " + name)
    file.close()
    bot.send_message(message.chat.id, "Що саме ви хочете замовити?")
    bot.register_next_step_handler(message, order_end)

def order_end(message):
    #print(message.text)
    tempID = str(message.from_user.id)
    way = '/orders/' + tempID
    file = open(way, 'a')
    name = str(message.text)
    file.write("\nДані замовлення: " + name)
    file.close()

    file = open(way, 'r')
    data = file.read()
    #print(data)
    file.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('< Повернутися на початок')
    bot.send_message(message.chat.id, "Замовлення " + tempID + "\n\n" + data + '\n\nДякуємо! Замовлення створене, очікуйте дзвінок оператора.', reply_markup=markup)

# order end

@bot.message_handler(content_types=['contact'])
def read_contact_phone(message):
    phone_usm = message.contact.phone_number
    if phone_usm[:4] == '+380' or phone_usm[:3] == '380':
        tempID = str(message.from_user.id)
        way = '/users/' + tempID
        file = open(way, 'w')
        username = str(message.from_user.username)
        first_name = message.from_user.first_name
        try:
            last_name = str(message.from_user.last_name)
        except:
            last_name = ''
        name = first_name + ' ' + last_name
        file.write(tempID + '\n' + username + '\n' + name + '\n' + 'user' + '\n' + phone_usm)
        file.close()
        bot.send_message(message.chat.id,
                        "Як ми можемо до Вас звертатись? (Бажано ім'я та прізвище)")
        bot.register_next_step_handler(message, reg_end)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_menu = types.KeyboardButton(text="< Повернутися на початок")
        keyboard.add(button_menu)
        bot.send_message(message.chat.id,
                         "Вибачте, але зареєструватись можуть тільки люди з номерами України.",
                         reply_markup=keyboard)

    # Реєстрація end

@bot.message_handler(content_types=['photo'])
def photo(message):
    print(message.photo[2].file_id)


@bot.message_handler(content_types=['video'])
def photo(message):
    print(message.video.file_id)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'other1':
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        previous = types.InlineKeyboardButton('<', callback_data='previous1')
        markup.add(previous)
        bot.send_video(call.message.chat.id,
                       "BAACAgIAAxkBAAOQY1Z_VtvkWbApRsWbGeDGIk6OX3YAAkkiAAIk7HhKHqSEMsUXJwQqBA",
                       caption="***Набір значків Ріж русню та ЦПР***\n\nКолір: Чорний\nЦіна: 300 грн (якщо треба два однакових - вкажіть це в коментарях при замовлені)",
                       reply_markup=markup, parse_mode="Markdown")
    if call.data == 'previous1':
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        other = types.InlineKeyboardButton('>', callback_data='other1')
        markup.add(other)
        bot.send_photo(call.message.chat.id,
                       "AgACAgIAAxkBAANZY1Z1o5w44LX2Jks_aeSe_pP9y5wAAvq8MRvogrhKwwXO5wchFKIBAAMCAAN5AAMqBA",
                       "***Чашка Ріж русню***\n\nКолір: Чорний\nЦіна: 300 грн (при замовленні від 2 чашок ціна 250грн або комплект футболка + чашка = 850грн)",
                       reply_markup=markup, parse_mode="Markdown")

bot.infinity_polling()
