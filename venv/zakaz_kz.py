from aiogram.dispatcher.filters.state import StatesGroup, State
from lo import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from string import Template
from aiogram.dispatcher import FSMContext


class TEST(StatesGroup):
    Q1 = State() # name of the person who ordered
    Q2 = State() # tele_number
    Q3 = State() # address
    Q4 = State() # payment of system
@dp.message_handler(Command('order_ps'), state=None)
async def start_order_kz(message: types.Message):
    await message.answer("Есіміңіз?")
    await TEST.Q1.set()

@dp.message_handler(state=TEST.Q1)
async def qu1(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("Телефон номеріңіз📱")
    await TEST.next()

@dp.message_handler(state=TEST.Q2)
async def qu2(message: types.Message, state=FSMContext):
    answer = int(message.text)
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Қай жерге жеткіземіз")
    await TEST.next()

@dp.message_handler(state=TEST.Q3)
async def qu3(message: types.Message, state=FSMContext):
    answer = message.text
    global ans3
    ans3 = answer
    await state.update_data(answer3 = answer)
    await message.answer("Төлем жүйесін таңдаңыз(Каспий/купюро)")
    await TEST.next()


@dp.message_handler(state=TEST.Q4)
async def qu4(message: types.Message, state=FSMContext):
    answer = message.text
    global ans4
    ans4 = answer
    type_of_console = "Play Station"
    t = Template('Тип консолю: $console\n Имя: $name\n Телефон номер: $number\n Аддрес доставки: $address\n Способ платежей: $payments')
    info = t.substitute(dict(console=type_of_console, name=ans1, number=ans2, address=ans3, payments=ans4))
    await state.update_data(answer4 = answer)
    data = await state.get_data()
    await bot.send_message(chat_id='@yerekerun', text=info)
    await bot.send_message(message.from_user.id, "Тапсырыс бергенңізге рақмет👍🏻, 60-120минут ішінде жеькізіледі🚛. Толық төлемді жеткізілген соң төлесеңіз болады😉")
    await state.finish()




