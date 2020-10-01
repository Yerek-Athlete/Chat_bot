from aiogram.dispatcher.filters.state import StatesGroup, State
from lo import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from string import Template
from aiogram.dispatcher import FSMContext

class Test(StatesGroup):
    Q1 = State() # name of the set
    Q2 = State() # how many spons
    Q3 = State() # name of the person(who give order)
    Q4 = State() # tele_number
    Q5 = State() # address

@dp.message_handler(Command("order"), state=None)
async def start_order(message: types.Message):
    await message.answer("Сеттің аты")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def qu1(message: types.Message, state: FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("таяқша саны")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def qu2(message: types.Message, state: FSMContext):
    answer = int(message.text)
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Есіміңіз")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def qu3(message: types.Message, state: FSMContext):
    answer = message.text
    global ans3
    ans3 = answer
    await state.update_data(answer3 = answer)
    await message.answer("Телефон номеріңізді")
    await Test.next()
@dp.message_handler(state=Test.Q4)
async def qu4(message: types.Message, state: FSMContext):
    answer = int(message.text)
    global ans4
    ans4 = answer
    await state.update_data(answer4 = answer)
    await message.answer("Мекен-жайыңызды")
    await Test.next()
@dp.message_handler(state=Test.Q5)
async def qu5(message: types.Message, state: FSMContext):
    answer = message.text
    global ans5
    ans5 = answer

    t = Template('Имя сета: $name_set \n Количества палок: $amount \n Имя: $name \n Телефон: $number \n Аддресс: $address')
    a = t.substitute({
        'name_set': ans1
        'amount': ans2
        'name': ans3
        'number': ans4
        'address': ans5
    })
    await state.update_data(answer5 = answer)
    data = await state.get_data()
    answer5 = data.get("answer5")
    await bot.send_message(chat_id='@yerekerun', text=a)
    await bot.send_message(message.from_user.id, "тапсырысыңыз қабылданды тапсырысыңыз 60-90 минут ішінде жеткізіледі")
    await state.finish()


