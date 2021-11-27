from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from current_users import current_user_states


class UserStateFilter(BoundFilter):
    """
    Фильтр который проверяет в каком состоянии находится покупатель.

    Атрибуты:

    user_state_name (str): имя состояния, которому должен соответствовать покупатель
    """

    key = 'user_state_name'

    def __init__(self, user_state_name: str):
        self.user_state_name = user_state_name

    async def check(self, message: types.Message) -> bool:
        user_state = current_user_states.get(message.from_user['id'])
        return user_state is not None and user_state.state == self.user_state_name
