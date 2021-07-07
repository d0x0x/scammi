import logging
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="1873178780:AAF5HzgUyoDxMMEhY-26o7HNoEoD7Fnc8ZI", parse_mode=types.ParseMode.HTML)
keyboard = types.InlineKeyboardMarkup()
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Hacking🔒", "Profile💼"]
    buttons2 = ["Оформить подписку"]
    keyboard.add(*buttons)
    keyboard.add(*buttons2)
    await message.answer("Добро пожаловать! Воспользуйся меню ниже🍃", reply_markup=keyboard)


############################################################################

btn = InlineKeyboardButton("VKONTAKTE", callback_data="cb")
btn2 = InlineKeyboardButton("INSTAGRAM", callback_data="cb2")
btn3 = InlineKeyboardButton("TELEGRAM", callback_data="cb3")
btn4 = InlineKeyboardButton("САЙТ ЕГЭ", callback_data="cb4")
btn5 = InlineKeyboardButton("TikTok", callback_data="cb5")
btn6 = InlineKeyboardButton("Facebook", callback_data="cb6")

btn_keyboard = InlineKeyboardMarkup(row_width=6).row(btn, btn2, btn3, btn4, btn5, btn6)

btn_keyboard = InlineKeyboardMarkup().add(btn, btn2, btn3, btn4, btn5, btn6)

@dp.message_handler()
async def any_text_message(message: types.Message):
    if message.text == 'Hacking🔒':
        await bot.send_message(message.from_user.id, '''Выберите что хотите взломать:''', parse_mode='Markdown', reply_markup=btn_keyboard)

    if message.text == 'Profile💼':
            await bot.send_message(message.from_user.id, f'''
            	⚗️ID : {message.from_user.id}
💊Баланс : 0''', parse_mode='Markdown')

    if message.text == 'Оформить подписку':
    	await bot.send_message(message.from_user.id, f'''
❓Как купить подписку?
✅Переведите на карту сумму 150 рублей : 4890 4947 4095 9424
♻️К коментарию платежа добавьте цифры {message.from_user.id}
⚠️Все платежа проводяться автоматически с помощью робота!''', parse_mode='Markdown')
        
@dp.callback_query_handler(lambda c: c.data == "cb")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "Оформите подписку!", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb2")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "Оформите подписку!", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb3")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "Оформите подписку!", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb4")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "Оформите подписку!", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb5")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "Оформите подписку!", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb6")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "Оформите подписку!", show_alert=True)

##########################################################################################

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)