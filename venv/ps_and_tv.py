from aiogram.dispatcher.filters.state import StatesGroup, State
from lo import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from string import Template
from aiogram.dispatcher import FSMContext


global co
co = "PS+TV"
class Check(StatesGroup):
    qu1 = State() # name of the person who ordered
    qu2 = State() # tele_number
    qu3 = State() # address
    qu4 = State() # payment of system
@dp.message_handler(Command('ps_tv'), state=None)
async def START_ORDER(message: types.Message):
    await message.answer("Ваше имя?")
    await Check.qu1.set()

@dp.message_handler(state=Check.qu1)
async def Ques1(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer(" Напишите свой номер, что бы мы вас не потеряли 😉📱")
    await Check.next()

@dp.message_handler(state=Check.qu2)
async def Ques2(message: types.Message, state=FSMContext):
    answer = int(message.text)
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Куда вам доставит?")
    await Check.next()

@dp.message_handler(state=Check.qu3)
async def Ques3(message: types.Message, state=FSMContext):
    answer = message.text
    global ans3
    ans3 = answer
    await state.update_data(answer3 = answer)
    await message.answer("Выберите способ оплаты(Каспий/налиный)")
    await Check.next()


@dp.message_handler(state=Check.qu4)
async def Ques4(message: types.Message, state=FSMContext):
    answer = message.text
    global ans4
    ans4 = answer

    t = Template('Тип консолa: $console\n Имя: $name\n Телефон номер: $number\n Аддрес доставки: $address\n Способ платежей: $payments')
    infor = t.substitute({'console': co, 'name': ans1, 'number': ans2, 'address': ans3, 'payments': ans4})
    await state.update_data(answer4 = answer)
    data = await state.get_data()
    await bot.send_message(chat_id='@yerekerun', text=infor)
    await bot.send_message(message.from_user.id, "Оплату можете на месте сделать, в течение 60-120мин доставим😉")
    await state.finish()




