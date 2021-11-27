from bot_text import *

user_requests_text = ['/start', 'большую', 'наличными', 'да', 'ЕЩЕ!',
                      '/help', '/start', 'среднюю', 'маленькую', 'яндекс деньги', 'картой', 'нет', '/stop']
bot_answers = [
    GREETING_TEXT,
    CHOOSE_PAYMENT_METHOD,
    ORDER_CONFIRMATION_TEXT.format(pizza='большую', payment_method='наличными'),
    END_SCENARIO_TEXT,
    COMMON_TEXT,
    HELP_TEXT,
    GREETING_TEXT,
    CHOOSE_PIZZA_TEXT,
    CHOOSE_PAYMENT_METHOD,
    CHOOSE_PAYMENT_METHOD,
    ORDER_CONFIRMATION_TEXT.format(pizza='маленькую', payment_method='картой'),
    REPEAT_SCENARIO_TEXT,
    STOP_ORDER_TEXT,
]
