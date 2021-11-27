# bot answers
HELP_TEXT = (f"Доступные команды:\n"
             f"- /start - начать заказ пиццы\n"
             f"- /help - помощь, список доступных команд\n"
             f"- /stop - прекратить заказ пиццы")
GREETING_TEXT = "Привет!\nЯ помогу заказать вам пиццу!\nКакую пиццу хотите большую или маленькую?"
STOP_ORDER_TEXT = "Заказ остановлен."
CHOOSE_PIZZA_TEXT = "Пожалуйста, выберите пиццу."
CHOOSE_PAYMENT_METHOD = "Пожалуйста, выберите способ оплаты."
ORDER_CONFIRMATION_TEXT = "Вы хотите {pizza} пиццу, оплата - {payment_method}"
REPEAT_SCENARIO_TEXT = "Начнем заказ сначала\nКакую пиццу хотите большую или маленькую?"
END_SCENARIO_TEXT = "Спасибо за заказ, чтобы сделать еще один введите /start"

# available answers
POSITIVE_ANSWER = "да"
AVAILABLE_PIZZAS = ["большую", "маленькую"]
AVAILABLE_PAYMENT_METHODS = ["наличными", "картой"]
AVAILABLE_ORDER_CONFIRMATION = [POSITIVE_ANSWER, "нет"]
