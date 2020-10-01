from aiogram.dispatcher.filters.state import StatesGroup, State
from lo import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from string import Template
from aiogram.dispatcher import FSMContext


global con
con = "PS+TV"
class Test(StatesGroup):
    Q1 = State() # name of the person who ordered
    Q2 = State() # tele_number
    Q3 = State() # address
    Q4 = State() # payment of system
@dp.message_handler(Command('order_ps_tv'), state=None)
async def start_order_kz(message: types.Message):
    await message.answer("Есіміңіз?")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def Qu1(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("Телефон номеріңіз📱")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def Qu2(message: types.Message, state=FSMContext):
    answer = int(message.text)
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Қай жерге жеткіземіз")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def Qu3(message: types.Message, state=FSMContext):
    answer = message.text
    global ans3
    ans3 = answer
    await state.update_data(answer3 = answer)
    await message.answer("Төлем жүйесін таңдаңыз")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def Qu4(message: types.Message, state=FSMContext):
    answer = message.text
    global ans4
    ans4 = answer

    t = Template('Тип консолa: $console\n Имя: $name\n Телефон номер: $number\n Аддрес доставки: $address\n Способ платежей: $payments')
    infor = t.substitute({'console': con, 'name': ans1, 'number': ans2, 'address': ans3, 'payments': ans4})
    await state.update_data(answer4 = answer)
    data = await state.get_data()
    await bot.send_message(chat_id='@yerekerun', text=infor)
    await bot.send_message(message.from_user.id, "Тапсырыс бергенңізге рақмет👍🏻, 60-120минут ішінде жеькізіледі🚛. Толық төлемді жеткізілген соң төлесеңіз болады😉")
    await state.finish()




