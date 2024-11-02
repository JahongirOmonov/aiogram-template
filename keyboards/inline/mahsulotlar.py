from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import course_callback
from loader import dp

mahsulotlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kurslar", callback_data="courses"),
         InlineKeyboardButton(text="Kitoblar", callback_data="buy")],

        [InlineKeyboardButton(text="Asosiy manba", url="https://t.me/kunuz")],
        [InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="Ulashish", switch_inline_query="zo'r ekan")]
    ],
)

coursesMenu = InlineKeyboardMarkup(row_width=1)
python = InlineKeyboardButton(text="Python dasturlash asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

