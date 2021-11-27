"""
Телеграм-бот для заказа пиццы.
Название бота: PythonTestPizzaBot.
"""
import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from bot_text import *
from telegram_supporting_functions import make_key_board, add_new_customer, delete_cur_customer, get_cur_customer, \
    set_chosen_pizza, set_chosen_payment_method
from telegram_filters import UserStateFilter

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.filters_factory.bind(UserStateFilter, event_handlers=[dp.message_handlers])


@dp.message_handler(commands=['start'])
async def start_order(message: types.Message):
    """По команде /start отправляет приветственное сообщение и начинает заказ."""
    add_new_customer(message.from_user['id'])
    keyboard = make_key_board(*AVAILABLE_PIZZAS, '/stop')

    await message.reply(GREETING_TEXT, reply_markup=keyboard)


@dp.message_handler(commands=['stop'])
async def stop_order(message: types.Message):
    """По команде /stop останавливает заказ."""
    delete_cur_customer(message.from_user['id'])
    keyboard = make_key_board('/start', '/help')

    await message.reply(STOP_ORDER_TEXT, reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    """По команде /help отправляет список доступных команд."""
    keyboard = make_key_board('/start', '/help')
    await message.reply(HELP_TEXT, reply_markup=keyboard)


@dp.message_handler(UserStateFilter(user_state_name='choose_pizza'))
async def choose_pizza(message: types.Message):
    """Обработка сообщения о выборе пиццы."""
    user_answer = message.text.lower()
    if user_answer not in AVAILABLE_PIZZAS:
        keyboard = make_key_board(AVAILABLE_PIZZAS, '/stop')
        await message.answer(CHOOSE_PIZZA_TEXT, reply_markup=keyboard)
        return

    set_chosen_pizza(message.from_user['id'], user_answer)
    keyboard = make_key_board(AVAILABLE_PAYMENT_METHODS, '/stop')
    await message.answer(CHOOSE_PAYMENT_METHOD, reply_markup=keyboard)


@dp.message_handler(UserStateFilter(user_state_name='choose_payment_method'))
async def choose_payment_method(message: types.Message):
    """Обработка сообщения о выборе способа оплаты."""
    user_answer = message.text.lower()
    if user_answer not in AVAILABLE_PAYMENT_METHODS:
        keyboard = make_key_board(*AVAILABLE_PAYMENT_METHODS, '/stop')
        await message.answer(CHOOSE_PAYMENT_METHOD, reply_markup=keyboard)
        return

    customer = set_chosen_payment_method(message.from_user['id'], user_answer)
    keyboard = make_key_board(*AVAILABLE_ORDER_CONFIRMATION, '/stop')
    await message.answer(ORDER_CONFIRMATION_TEXT.format(pizza=customer.chosen_pizza,
                                                        payment_method=customer.chosen_payment_method),
                         reply_markup=keyboard)


@dp.message_handler(UserStateFilter(user_state_name='order_confirmation'))
async def order_confirmation(message: types.Message):
    """Обработка сообщения о подтверждении заказа."""
    user_id = message.from_user['id']
    customer = get_cur_customer(user_id)

    user_answer = message.text.lower()
    if user_answer not in AVAILABLE_ORDER_CONFIRMATION:
        keyboard = make_key_board(*AVAILABLE_ORDER_CONFIRMATION, '/stop')
        await message.answer(ORDER_CONFIRMATION_TEXT.format(pizza=customer.chosen_pizza,
                                                            payment_method=customer.chosen_payment_method),
                             reply_markup=keyboard)
        return

    if user_answer == POSITIVE_ANSWER:
        delete_cur_customer(user_id)
        keyboard = make_key_board('/start', '/help')
        await message.answer(END_SCENARIO_TEXT, reply_markup=keyboard)
        return
    else:
        customer.next()
        keyboard = make_key_board(*AVAILABLE_PIZZAS, '/stop')
        await message.answer(REPEAT_SCENARIO_TEXT, reply_markup=keyboard)


@dp.message_handler()
async def go_to_start_order(message: types.Message):
    """Обработка сообщения, когда пользователь находится вне нашего сюжета."""
    keyboard = make_key_board('/start', '/help')
    await message.answer(f"Вы еще не начали заказ, если хотите заказать пиццу введите /start "
                         f"для справки введите /help", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
