from aiogram import types
from order import order
#from order_full import order_full
#from states import states
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from lo import bot, dp

b1 = KeyboardButton('kz🇰🇿')
b2 = KeyboardButton('ru🇷🇺')
b3 = KeyboardButton('eng🇺🇸')

markup_language = ReplyKeyboardMarkup().row(
    b1, b2, b3
)

inline_set = InlineKeyboardMarkup(row_width=3)
set_diplom = InlineKeyboardButton('Дипломат🍣', callback_data='diplomat')
set_posi = InlineKeyboardButton('Позитивчик🍣', callback_data='posi')
set_bar = InlineKeyboardButton('Бармаглот🍣', callback_data='barmaglog')
set_he_she = InlineKeyboardButton('Он и Она🍣', callback_data='He_She')
inline_set.insert(set_diplom)
inline_set.insert(set_posi)
inline_set.insert(set_bar)
inline_set.insert(set_he_she)

Text = "Тілді таңдаңыз, пажалуиста выберите язык, please choose language"
text_kz = "сушиға🍣 тапсырыс беру үшін /sushi_kz басыңыз"
text_ru = "чтобы заказат суши🍣 нажмите кнопку /sushi_ru"
text_eng = "For order sushi🍣 press /suhi_eng"
text_else = "нажмите только кнопки"
text_else_kz = "тек қана кнопкаларды басыңыз"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text=Text, reply_markup=markup_language)

@dp.message_handler(commands=['sushi_kz'])
async def send_message(message: types.Message):
    await bot.send_message(message.from_user.id, text='Сетті таңдаңыз', reply_markup=inline_set)

@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    m = message.text
    if m == "kz🇰🇿":
        await bot.send_message(message.from_user.id, text=text_kz)
        #await bot.send_message(chat_id='@yerekerun', text="админ сука")
    elif m == "ru🇷🇺":
        await bot.send_message(message.from_user.id, text=text_ru)
    elif m == "eng🇺🇸":
        await bot.send_message(message.from_user.id, text=text_eng)
    else:
        await bot.send_message(message.from_user.id, text=text_else)

@dp.callback_query_handler(text='diplomat')
@dp.callback_query_handler(text='posi')
@dp.callback_query_handler(text='barmaglog')
@dp.callback_query_handler(text='He_She')
async def procces(call: types.CallbackQuery):
    answer_data = call.data
    if answer_data == 'diplomat':
        text = "✳Сет для студентов❗ \n Сет называется «𝐃𝐈𝐏𝐋𝐎𝐌𝐀𝐍𝐓 \nПримечание: \n-Покажите студенческий билет и получите сет со скидкой 4900тг \nВнимание: ТОЛЬКО НА ДОСТАВКУ \n——————————————————————\n60шт суши и одна пицца🔺\n🍣Филадельфия 10шт\n🍣Эби кинг с креветкой 10шт\n🍣Цезарь 10шт\n🍣Сяке темпура 10шт\n🍣Бонита 10шт\n🍣Ёжик в тумане 10шт\n🍕Пепперони пицца\n🍱Цена со скидкой = 4900тг🔔\n——————————————————————\n Тапсырыс беру үшін /order 📲 басыңыз"
    elif answer_data == 'posi':
        text = ""
    elif answer_data == 'barmaglog':
        text = ""
    elif answer_data == 'He_She':
        text = ""
    else:
        text = "Please choose in Inline buttons"
    await bot.send_message(call.from_user.id, text=text)



