from socket import socket, SOCK_STREAM, AF_INET
import logging
import time

import click

from common.utils import DataExchange as DE, FormAlertOrError as FAOE
from common.config import *
from log.server_log_config import Log


form_alert_or_error = FAOE().form_alert_or_error
get_data = DE.get_data
send_data = DE.send_data
logger = logging.getLogger('server')


# по сути это обработчик событий, не могу понять как правильно его
# построить и написать под него тесты
# вижу 2 варианта, либо через is DEBUG внутри функции ниже (+if), либо
# сокеты сразу передавать в виде аргумента, но так вроде не правильно
# тестировать
@Log()
def event_handler(sock: socket) -> dict:
    """ Handles requests from client """

    data = get_data(sock)

    logger.info(f'input data: {data}')

    if data is None or data.get('action') not in ACTIONS_TUPLE:
        send_data(sock, form_alert_or_error(400))

        return data

    if data.get('response'):
        return data

    if data.get('action') == 'presence':
        send_data(sock, form_alert_or_error(200))
        return data

    logger.info('Event is end!')

    return


@click.command()
@click.option('--addr', default=DEFAULT_IP_ADDRESS, help='ip address')
@click.option('--port', default=DEFAULT_SERVER_PORT, help='port number')
def command_line(addr: str, port: int):
    """ Listening port for some client to handles them.  \n
    Start in terminal:\n
    --addr: client's address (not required);\n
    --port: client's port (not required).  \n

    examples: \n
    python3.6 server.py;\n
    python3.6 server.py localhost --port 7777.

    """

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(SOCKET_LISTENING)

    while True:
        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            logger.info('Exception KeyboardInterrupt!')
            print('Ожидайте закрытия минуту.')

            time.sleep(60)

            raise

        else:
            event_handler(client)

        finally:
            client.close()


if __name__ == '__main__':
    command_line()
