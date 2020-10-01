from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from lo import dp
class Test(StatesGroup):
    Q1 = State()
    Q2 = State()

@dp.message_handler(Command("order"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1. \n\n"
                         "Вы часто занимаетесь бессмысленными делами "
                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, просто смотрите в потолок)?")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1 = answer)
    await message.answer("Сіз жауап бердіңіз!")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Жауаптарыңызға рақмет")
    await state.finish()

