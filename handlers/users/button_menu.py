from keyboards.default.menuButton import menuButton, pythonButton, contactButton
from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

@dp.message_handler(text="Menu")
async def menu(message: types.Message):
    await message.answer("Menu", reply_markup=menuButton)

@dp.message_handler(text="Ortga")
async def menu(message: types.Message):
    await message.answer("Menu", reply_markup=menuButton)

# @dp.message_handler(commands="start")
# async def start(message: types.Message):
#     await message.answer("Assalomu alaykum!\nMenu tugmasini bosing", reply_markup=contactButton)



@dp.message_handler(text="Python")
async def python(message: types.Message):
    fornow = "Darslardan  birini tanlang!"
    await message.answer(fornow, reply_markup=pythonButton)

@dp.message_handler(text="1-dars")
async def python_1(message: types.Message):
    await message.answer("1-dars\n...\n..\n.")

@dp.message_handler(text="2-dars")
async def python_1(message: types.Message):
    await message.answer("2-dars\n...\n..\n.")

@dp.message_handler(text="3-dars")
async def python_1(message: types.Message):
    await message.answer("3-dars\n...\n..\n.")


@dp.message_handler(content_types="contact")
async def contact(message: types.Message):
    if message.contact.user_id == message.from_user.id:
        await message.answer(f"Kontaktingiz o'zingizniki", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(f"Kontaktingiz o'zingizniki emas!")