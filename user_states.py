"""
Логика перехода между состояниями покупателя.
"""
from transitions import Machine


class Customer:
    """
    Класс покупателя.

    Атрибуты:

    chosen_pizza (str, None): выбранная покупателем пицца
    chosen_payment_method (str, None): выбранный покупателем способ оплаты
    """

    def __init__(self, id: str):
        self.id = id
        self.chosen_pizza = None
        self.chosen_payment_method = None


states = ['choose_pizza', 'choose_payment_method', 'order_confirmation']
transitions = [{'trigger': 'next', 'source': 'choose_pizza', 'dest': 'choose_payment_method'},
               {'trigger': 'next', 'source': 'choose_payment_method', 'dest': 'order_confirmation'},
               {'trigger': 'next', 'source': 'order_confirmation', 'dest': 'choose_pizza'}, ]


def get_customer(customer_id: str, initial_state: str = 'choose_pizza') -> Customer:
    """
    Добавление состояний и возможных переходов между этими состояниями к экземпляру класса Customer.
    Возвращает полученный экземпляр

    :param initial_state: начальное состояние экземпляра
    :type initial_state: str
    :param customer_id: уникальный идентификатор покупателя
    :type customer_id: str

    :return: экземпляр класса Customer
    :rtype: Customer
    """
    customer = Customer(customer_id)
    Machine(model=customer, states=states, transitions=transitions, initial=initial_state)

    return customer
