from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardButton, InlineKeyboardMarkup
from config import Token

TOKEN = '1270237768:AAFFEyzePLDVh7-HSDMtiFcCDSJ-iVNyosI'
bot = Bot(token=Token)
dp = Dispatcher(bot)

button_hi = KeyboardButton('Hi!')
greet = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

b1 = KeyboardButton('1')
b2 = KeyboardButton('2')
b3 = KeyboardButton('3')

markup = ReplyKeyboardMarkup().add(
    b1).add(b2).add(b3)

markup_2 = ReplyKeyboardMarkup().row(
    b1, b2, b3
)
markup_1 = ReplyKeyboardMarkup().row(
    b1, b2, b3
).add(KeyboardButton('Middle row'))

b4=KeyboardButton('4')
b5=KeyboardButton('5')
b6=KeyboardButton('6')
markup_1.row(b4, b5)
markup_1.insert(b6)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Send own contact', request_contact=True)
).add(
    KeyboardButton('Send your location', request_location=True)
)

'''choice = InlineKeyboardMarkup(row_width=2)
buy_thing = InlineKeyboardButton(text="Buy apple", callback_data='ok')
choice.insert(buy_thing)
buy_thing_1 = InlineKeyboardButton(text="Buy raspberri", callback_data='OK')
choice.insert(buy_thing_1)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data='cancel')
choice.insert(cancel_button)'''


#@dp.callback_query_handler(func=lambda c: c.data == 'ok')

inline_b = InlineKeyboardMarkup(row_width=2)
inline1 = InlineKeyboardButton('First button', callback_data = 'b1')
inline2 = InlineKeyboardButton('Second button', callback_data = 'b2')
cancell_button = InlineKeyboardButton('cancel', callback_data='cancel')
inline_b.insert(inline1)
inline_b.insert(inline2)
inline_b.insert(cancell_button)

@dp.message_handler(commands=['inline'])
async  def show_info(message: types.Message):
    await message.answer(text="For sell we have apple and raspberri", reply_markup=inline_b)

@dp.callback_query_handler(text = 'b1')
@dp.callback_query_handler(text='b2')
@dp.callback_query_handler(text = 'cancel')
async def process(call: types.CallbackQuery):
    answer_data = call.data
    #call.answer(f'you pressed one of the button here!')

    if answer_data == 'b1':
       # await bot.send_message(call.from_user.id, 'first button pressed!')
       text = 'first button pressed👍🏻'
    elif answer_data == 'b2':
        #await bot.send_message(call.from_user.id, 'second buttin was pressed')
        text = 'second button pressed👍🏻'
    elif answer_data == 'cancel':
        text = 'you was press button of cancel 🖕🏻'
    else:
        text = 'please press one of the buttons'
    await bot.send_message(call.from_user.id, text)
   # await bot.answer_callback_query(call.id)
    #await bot.send_message(call.from_user.id, 'first button pressed!')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "please choose button: /button or /but_1", reply_markup=markup_1 )

@dp.message_handler(commands=['button'])
async def send_button(message: types.Message):
    await message.reply("Hi write smth", reply_markup=greet)

@dp.message_handler(commands=['but_1'])
async def send(message: types.Message):
    await bot.send_message(message.from_user.id, "Okk", reply_markup=markup_2)
@dp.message_handler(commands=['but2'])
async def contact_and_geo(message: types.Message):
    await bot.send_message(message.from_user.id, "Please give allow for get information in your phone!", reply_markup=markup_request)
    await bot.send_message(chat_id='@yerekerun', text='You are athlet!')
dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    #caption = 'телеграм'
    await bot.send_photo(message.fr, photo="https://play.google.com/store/apps/details?id=org.telegram.messenger&hl=ru", caption="Telegram")





@dp.message_handler(commands=['remove'])
async def remove(message: types.Message):
    await message.reply("delete all button", reply_markup=ReplyKeyboardRemove())




@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp)



