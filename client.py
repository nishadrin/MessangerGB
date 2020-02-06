from socket import socket, SOCK_STREAM, AF_INET
import logging

import click

from common.utils import DataExchange as DE, FormAlertOrError as FAOE
from common.form_request_client import presence_msg
from common.config import *
from log.client_log_config import Log


form_alert_or_error = FAOE().form_alert_or_error
get_data = DE.get_data
send_data = DE.send_data
logger = logging.getLogger('client')


@Log()
def event_handler(sock: socket) -> dict:
    """ Handles requests from server """

    data = get_data(sock)

    logger.info(f'input data: {data}')

    if data is None or data.get('action') not in ACTIONS_TUPLE:
        send_data(sock, form_alert_or_error(400))

        return data

    if data.get('response'):
        return data

    if data.get('action') == 'probe':
        send_data(sock, presence_msg('Nick'))

        return data

    return


@click.command()
@click.argument('addr')
@click.option('--port', type=int, help="server's port")
def command_line(addr: str, port: int):
    """ Connect with server to send request and get response with
    handler processing.  \n
    Start in terminal:  \n
    addr - server's address;  \n
    --port - server's port.  \n

    example: python3.6 client.py localhost --port 7777.
    
    """

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    send_data(sock, presence_msg('Nick'))

    event_handler(sock)

    sock.close()


if __name__ == '__main__':
    command_line()
