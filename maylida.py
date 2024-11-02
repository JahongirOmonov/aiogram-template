# from aiogram import types, Dispatcher, executor, Bot
# from aiogram.dispatcher.filters import CommandStart
# from aiogram.types import CallbackQuery
#
# from keyboards.inline.mahsulotlar import mahsulotlar
#
# bot = Bot(token='7550438556:AAE2GLsBH45dJYSVTTJYQKeMstk22ieJZ6I', parse_mode=types.ParseMode.HTML)
# dp = Dispatcher(bot)
#
# async def keyboards():
#     return types.InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 types.InlineKeyboardButton(text="Mahsulotlar", callback_data="courses")
#             ]
#         ]
#     )
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=await keyboards())
#
# @dp.callback_query_handler(lambda call: call.data == "courses")
# async def products(call: CallbackQuery):
#     print(call.data)
#     await call.message.answer("Kurs tanlang")
#     await call.answer()
#
#
#
#
# executor.start_polling(dp)
#


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
API_TOKEN = '7550438556:AAE2GLsBH45dJYSVTTJYQKeMstk22ieJZ6I'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Create inline keyboard
def get_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Option 1", callback_data="option1"),
        InlineKeyboardButton(text="Option 2", callback_data="option2"),
        InlineKeyboardButton(text="Option 3", callback_data="option3"),
        InlineKeyboardButton(text="Option 4", callback_data="option4")
    ]
    keyboard.add(*buttons)
    return keyboard


# Command handler for /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Hello! Choose an option:",
        reply_markup=get_keyboard()
    )


# Callback query handler
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('option'))
async def process_callback(callback_query: types.CallbackQuery):
    # Get the callback data
    option = callback_query.data

    # Different responses based on the selected option
    responses = {
        'option1': 'You selected Option 1!',
        'option2': 'You selected Option 2!',
        'option3': 'You selected Option 3!',
        'option4': 'You selected Option 4!'
    }

    # Answer the callback query to remove the loading state
    await bot.answer_callback_query(callback_query.id)

    # Edit the message with the response
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=responses[option],
        reply_markup=get_keyboard()  # Keep the keyboard
    )


# Error handler
@dp.errors_handler()
async def errors_handler(update, exception):
    print(f"Update: {update}\nException: {exception}")
    return True


if __name__ == '__main__':
    # Start the bot
    executor.start_polling(dp, skip_updates=True)

