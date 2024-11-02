from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp

menuButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Telegram bot")
        ]
    ],
    resize_keyboard=True
)

pythonButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-dars"),
            KeyboardButton(text="2-dars"),
            KeyboardButton(text="3-dars"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Oldinga"),
        ],
    ],
    resize_keyboard=True
)

contactButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
            KeyboardButton(text="Location", request_location=True),
        ],
    ],
    resize_keyboard=True
)

wtfButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar"),
            KeyboardButton(text="Boshqa narsalar"),
        ]
    ],
    resize_keyboard=True


)