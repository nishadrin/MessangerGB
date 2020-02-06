from functools import wraps
import logging
import inspect


_file = 'client'
format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(module)s | %(message)s"
    )

logger = logging.getLogger(_file)

time_file_handler = logging.FileHandler(f'{_file}.log', encoding='utf-8')
time_file_handler.setLevel(logging.DEBUG)
time_file_handler.setFormatter(format)

logger.addHandler(time_file_handler)
logger.setLevel(logging.DEBUG)


class Log():

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f'funcion before: {inspect.stack()[1][3]} | name:'
                        f' {func.__name__} | input args and kwargs: '
                        f'{args}, {kwargs}')

            return func(*args, *kwargs)

        return wrapper
