import logging, config
from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

class Test(StatesGroup):
    Q1 = State()
    Q2 = State()

bot = Bot(token=config.Token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )



@dp.message_handler(Command("test"), state=None)
async def start_test(msg: types.Message):
    await msg.answer("Сіз тесті бастадыңыз!")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def ans1(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(answer1 = answer)
    await msg.answer("Сіз 1-ші сұраққа жауап бердіңіз!")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def ans2(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    ans1 = data.get("answer1")
    ans2 = msg.text

    await msg.answer("Сіз барлық сұрақтарға жауап бердіңіз!")
    await state.finish()

'''async def on_shut(dp):
    await bot.close()
    await storage.close()



if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dp, on_shut=on_shut)
'''