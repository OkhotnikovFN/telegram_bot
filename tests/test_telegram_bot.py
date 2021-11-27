import unittest
from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock

from aiogram import executor, types


class TestChatBot(TestCase):
    MESSAGE_PATTERN = {"message_id": 634,
                       "from": {"id": 1111111111, "is_bot": False, "first_name": "FirstName", "last_name": "LastName",
                                "username": "UserName", "language_code": "ru"},
                       "chat": {"id": 1111111111, "first_name": "FirstName", "last_name": "LastName",
                                "username": "UserName", "type": "private"}, "date": 1637945326, "text": ""}

    def test_run_ok(self):

        messages = []
        for input_text in ['a', 'b', 'c']:
            message = deepcopy(self.MESSAGE_PATTERN)
            message['text'] = input_text
            messages.append([types.Message(**message)])

        long_poller_mock = Mock()
        long_poller_mock.get_updates = Mock(return_value=messages)

        async def qqq():
            return {'aaa': 'sad'}

        # TODO Тест не доделан
        # with patch('aiogram.executor.Executor._welcome', return_value=Mock()):
        with patch('aiogram.bot.api.check_token', return_value=True):
            with patch('os.getenv', return_value='1234:testtest'):
                with patch('aiogram.bot.api.make_request', return_value=qqq()):
                    from telegram_bot_server import dp
                    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    unittest.main()
