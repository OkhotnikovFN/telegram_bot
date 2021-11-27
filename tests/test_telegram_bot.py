import asyncio
import logging
from copy import deepcopy
import unittest
from unittest import TestCase
from unittest.mock import patch

from aiogram import executor, types

from test_scenario import user_requests_text, bot_answers


class TestChatBot(TestCase):
    MESSAGE_PATTERN = {"message_id": 634,
                       "from": {"id": 1111111111, "is_bot": False, "first_name": "FirstName", "last_name": "LastName",
                                "username": "UserName", "language_code": "ru"},
                       "chat": {"id": 1111111111, "first_name": "FirstName", "last_name": "LastName",
                                "username": "UserName", "type": "private"}, "date": 1637945326, "text": "1"}
    UPDATE_PATTERN = {'update_id': 234, 'message': MESSAGE_PATTERN}

    def test_scenario(self):
        """
        Тестирует правильность обработки сценария, происходит проверка на количество ответов бота требуемому
        и проверка что ответы соответствуют ожидаемым.
        """
        logging.disable()

        updates = []
        for input_text in user_requests_text:
            message = deepcopy(self.MESSAGE_PATTERN)
            message['text'] = input_text
            update = deepcopy(self.UPDATE_PATTERN)
            update['message'] = message
            updates.append(update)

        async def mock_request():
            return self.MESSAGE_PATTERN

        async def mock_get_updates(updates):
            asyncio.get_event_loop().stop()
            update_types = [types.Update(**update) for update in updates]
            return update_types

        future_request = asyncio.ensure_future(mock_request())
        future_get_updates = asyncio.ensure_future(mock_get_updates(updates))
        test_answers = []

        with patch('os.getenv', return_value='1234:testtest'):
            with patch('aiogram.bot.api.check_token', return_value=True):
                with patch('aiogram.bot.api.make_request', return_value=future_request):
                    with patch('aiogram.bot.Bot.get_updates', return_value=future_get_updates):
                        with patch('aiogram.bot.Bot.send_message', return_value=future_get_updates) as send_messages:
                            from telegram_bot_server import dp
                            executor.start_polling(dp, skip_updates=True)
                            for args, kwargs in send_messages.call_args_list:
                                test_answers.append(kwargs['text'])

        self.assertEqual(len(test_answers), len(bot_answers))
        for test_answer, bot_answer in zip(test_answers, bot_answers):
            self.assertEqual(test_answer, bot_answer)


if __name__ == '__main__':
    unittest.main()
