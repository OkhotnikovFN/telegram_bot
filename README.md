# Простой [телеграм бот](https://t.me/PythonTestPizzaBot) с коротким диалогом

___
## Используемый стэк:
- [aiogram](https://pypi.org/project/aiogram/) (фреймворк для работы с API telegram)
- [transitions](https://pypi.org/project/transitions/) (Стейт-машина)

## Установка и запуск
- копировать репозиторий на свою машину
- установить зависимости из requirements.txt (```pip install -r requirements.txt```)  
- установить переменную окружения __TELEGRAM_BOT_TOKEN__ с токеном вашего бота (нужно взять в телеграм у [@BotFather](https://t.me/BotFather))
- запустить telegram_bot_server.py (```python telegram_bot_server.py```)

## Комментарии
- база здесь не подключена, по-хорошему вместо переменной __'current_user_states'__, все данные нужно хранить в базе для данного примера вполне подойдет sqlite, там же хранить заказы (но в другой таблице), сейчас они нигде не сохраняются
- __Procfile__ нужен исключительно для того, чтобы развернуть приложение на [heroku](https://www.heroku.com).
