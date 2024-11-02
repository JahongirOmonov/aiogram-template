from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from loader import dp
from states.infoState import InfoState

@dp.message_handler(commands='begin', state=None)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"To`liq ismingizni kiriting! ")
    await state.set_state(InfoState.fullname)

@dp.message_handler(state=InfoState.fullname)
async def process_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"fullname": f"{fullname}"})
    await message.answer(f"Email manzilingizni kiriting")
    # await state.set_state(InfoState.email)
    await InfoState.next()


@dp.message_handler(state=InfoState.email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data({"email": f"{email}"})
    await message.answer(f"Telefon raqamingizni kiriting")
    await InfoState.next()

@dp.message_handler(state=InfoState.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data({"phone_number": f"{phone_number}"})
    data = await state.get_data()
    await message.answer(f"Ismingiz: {data['fullname']}\nEmail: {data['email']}\nTelefon raqam: {data['phone_number']}")
    await state.finish()
    # await state.reset_state(with_data=True)