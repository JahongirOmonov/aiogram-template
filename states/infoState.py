from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp

class InfoState(StatesGroup):
    fullname = State()
    email = State()
    phone_number = State()