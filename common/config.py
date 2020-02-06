DEBUG = False

DEFAULT_IP_ADDRESS = 'localhost'
DEFAULT_SERVER_PORT = 7777
SOCKET_LISTENING = 5

JIM_MAX_BYTES = 640
PROJECT_MAIN_PATH = '/home/nick/Документы/Проверка ДЗ/Клиент-серверные ' \
    'приложения на Python/lesson_3/'

ACTIONS_TUPLE = (
    'presence', # присутствие. Сервисное сообщение для извещения сервера
    # о присутствии клиента online
    'prоbe', # проверка присутствия. Сервисное сообщение от сервера для
    # проверки присутствии клиента online
    'msg', # простое сообщение пользователю или в чат
    'authenticate', # авторизация на сервере
    'quit', # отключение от сервера
    'join', # присоединиться к чату
    'leave', # покинуть чат
    )
ALERTS_MSGS = {
    '100': 'base notification',
    '101': 'important notification',
    '200': 'OK',
    '201': 'created',
    '202': 'accepted',
    '400': 'wrong request/JSON object',
    '401': 'not authorized',
    '402': 'wrong password or no account with that name',
    '403': 'forbidden',
    '404': 'not found chat or user',
    '409': 'conflict with another one connect',
    '410': 'gone offline',
    '500': 'server error',
    }

# поле action — 15 символов
# поле response — с кодом ответа сервера, это 3 цифры;
# имя пользователя / название чата (name): 25 символов;
# сообщение — максимум 500 символов (" ").
