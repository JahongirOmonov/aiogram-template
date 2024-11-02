from aiogram.dispatcher.filters import CommandStart
import logging

from aiogram.types import CallbackQuery

from keyboards.inline.mahsulotlar import mahsulotlar
from aiogram import types
from loader import dp
from keyboards.default.menuButton import wtfButton
from keyboards.inline.mahsulotlar import coursesMenu

@dp.callback_query_handler(lambda call: True)
async def products(call: CallbackQuery):
    print(call.data)
    logging.info(f"{call.from_user.full_name=} xxx")
    await call.message.answer("Kurs tanlang", reply_markup=coursesMenu)
    await call.answer()

@dp.message_handler(CommandStart(), state=None)
async def products(message: types.Message):
    # logging.info(f"{message.from_user.full_name=} ")
    await message.answer("Menuni tanlang", reply_markup=wtfButton)

@dp.message_handler(text="Mahsulotlar")
async def products(message: types.Message):
    await message.answer("Mahsulotlarni ttanlang", reply_markup=mahsulotlar)



