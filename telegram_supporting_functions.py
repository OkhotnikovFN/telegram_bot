from aiogram import types

from current_users import current_user_states
from user_states import get_customer, Customer


def make_key_board(*args: str) -> types.ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками.
    :param args: переданные названия кнопок
    :type args:  str

    :return: экземпляр клавиатуры
    :rtype: types.ReplyKeyboardMarkup
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*args)

    return keyboard


def add_new_customer(user_id: str) -> Customer:
    """
    Добавление покупателя в список обслуживаемых
    :param user_id: уникальный идентификатор покупателя
    :type user_id: str

    :return: экземпляр покупателя
    :rtype: Customer
    """
    customer = get_customer(user_id)
    current_user_states[user_id] = customer

    return customer


def delete_cur_customer(user_id: str) -> None:
    """
    Удаление покупателя в список обслуживаемых
    :param user_id: уникальный идентификатор покупателя
    :type user_id: str

    :return: экземпляр покупателя
    :rtype: Customer
    """
    current_user_states.pop(user_id, None)


def get_cur_customer(user_id: str) -> Customer:
    """
    Получить покупателя из списка обслуживаемых
    :param user_id: уникальный идентификатор покупателя
    :type user_id: str

    :return: экземпляр покупателя
    :rtype: Customer
    """
    return current_user_states.get(user_id)


def set_chosen_pizza(user_id: str, user_answer: str) -> Customer:
    """
    Записывает выбранную покупателем пиццу, в экземпляр класса Customer
    и переводит пользователя в следующее состояние.
    :param user_id: уникальный идентификатор покупателя
    :type user_id: str
    :param user_answer: ответ пользователя
    :type user_answer: str

    :return: экземпляр покупателя
    :rtype: Customer
    """
    customer = get_cur_customer(user_id)
    customer.chosen_pizza = user_answer
    customer.next()

    return customer


def set_chosen_payment_method(user_id: str, user_answer: str) -> Customer:
    """
    Записывает выбранный покупателем способ оплаты, в экземпляр класса Customer
    и переводит пользователя в следующее состояние.
    :param user_id: уникальный идентификатор покупателя
    :type user_id: str
    :param user_answer: ответ пользователя
    :type user_answer: str

    :return: экземпляр покупателя
    :rtype: Customer
    """
    customer = get_cur_customer(user_id)
    customer.chosen_payment_method = user_answer
    customer.next()

    return customer
