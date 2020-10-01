from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from lo import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

import zakaz_kz, ps_tv, zakaz_ru, ps_and_tv


b1 = KeyboardButton('Kz-kz')
b2 = KeyboardButton('Ru-ru')

markup_language = ReplyKeyboardMarkup().row(b1, b2)
Text = "Тіл таңдаңыз 🇰🇿 || Выберите язык 🇷🇺"
text_kz = "Сәлеметсіз бе 🙃, неге тапсырыс бересіз?) Ps4 / Ps4 + TV  Тапсырыс бергіңіз келсе /Tap түймесін басыңыз"
text_ru = "Добрый день🙃, что арендуем? Ps4 / Ps4 + TV Если хотите заказать, нажмите /zakaz"
text_else = "нажмите только кнопки"
text_else_kz = "тек қана кнопкаларды басыңыз"

support = "Техникалық қателер туындағанда админстратор номеріне хабарласыңыз📞: 87471850499\nВ случае технических ошибок звоните по номеру администратора📞: 87471850499 "


inline_devices = InlineKeyboardMarkup()
ps = InlineKeyboardButton("🎮 PS4", callback_data='ps')
ps_tv = InlineKeyboardButton("🎮 PS4+TV", callback_data='ps_tv')

inline_devices.insert(ps)
inline_devices.insert(ps_tv)

inline_ru = InlineKeyboardMarkup()
ps_ru = InlineKeyboardButton("🎮 PS4", callback_data='ps_ru')
ps_tv_ru = InlineKeyboardButton("🎮 PS4", callback_data='ps_tv_ru')
inline_ru.insert(ps_ru)
inline_ru.insert(ps_tv_ru)

@dp.message_handler(commands=['start'])
async def choose(message: types.Message):
    await bot.send_message(message.from_user.id, text=Text, reply_markup=markup_language)

@dp.message_handler(commands=['Tap'])
async def order_kz(message: types.Message):
    await bot.send_message(message.from_user.id, text='🎮 Kонсольды таңдаңыз', reply_markup=inline_devices)

@dp.message_handler(commands=['zakaz'])
async def order_ru(message: types.Message):
    await bot.send_message(message.from_user.id, text_ru, reply_markup=inline_ru)

@dp.message_handler(commands=['help'])
async def suppport(message: types.Message):
    await bot.send_message(message.from_user.id, text=support)

@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    m = message.text
    if(m == "Kz-kz"):
        await bot.send_message(message.from_user.id, text=text_kz)
    elif(m == "Ru-ru"):
        await bot.send_message(message.from_user.id, text=text_ru)
    else:
        await bot.send_message(message.from_user.id, text=text_else_kz)

@dp.callback_query_handler(text = 'ps')
@dp.callback_query_handler(text = 'ps_tv')
@dp.callback_query_handler(text = 'ps_ru')
@dp.callback_query_handler(text='ps_tv_ru')
async def proccess(call: types.CallbackQuery):
    data = call.data
    if(data == 'ps'):
        text = "Комплекте 7 ойын 🎮\n1)FIFA 20\n2) UFC 3\n3) Call Of Duty WWII\n4) GTA 5\n5) Mortal Kombat XL\n6) Tekken 7\n7) NFS Payback,\n🚛 Tапсырыс беру үшін /order_ps басыңыз"
    elif(data == 'ps_tv'):
        text = "Комплекте 7 ойын 🎮\n1)FIFA 20\n2) UFC 3\n3) Call Of Duty WWII\n4) GTA 5\n5) Mortal Kombat XL\n6) Tekken 7\n7) NFS Payback,\n🚛 Тапсырыс беру үшін /order_ps_tv басыңыз"
    elif(data == 'ps_ru'):
        text = "В комплекте 7 игр  🎮\n1)FIFA 20\n2) UFC 3\n3) Call Of Duty WWII\n4) GTA 5\n5) Mortal Kombat XL\n6) Tekken 7\n7) NFS Payback,\n🚛 чтобы заказывать нажмите /ps"
    elif(data == 'ps_tv_ru'):
        text = "В комплекте 7 игр  🎮\n1)FIFA 20\n2) UFC 3\n3) Call Of Duty WWII\n4) GTA 5\n5) Mortal Kombat XL\n6) Tekken 7\n7) NFS Payback,\n🚛 чтобы заказывать нажмите /ps_tv"
    else:
        text = "тауарды кнопкалардан таңдаңыз, выберите консоль с помощью кнопок"
    await bot.send_message(call.from_user.id, text=text)

