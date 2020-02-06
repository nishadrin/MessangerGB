import json
import socket
from datetime import datetime

from .config import JIM_MAX_BYTES, ALERTS_MSGS


class DataPacking:
    """ Pack/unpack data to json and encode/decode """

    def pack_data(data: dict, encoding: str) -> bytes:
        return json.dumps(data).encode(encoding)

    def unpack_data(data: bytes, encoding: str) -> dict:
        return json.loads(data.decode(encoding))


class DataExchange:
    """ Get/send, pack/unpack and encode/decode data """
    def get_data(sock: socket, encoding: str='ascii') -> dict:
        """ Get, decode and unpack data.
        return dict.

        """

        recieve_bytes: bytes = sock.recv(JIM_MAX_BYTES)

        if not recieve_bytes:
            return

        return DataPacking.unpack_data(recieve_bytes, encoding)

    def send_data(sock: socket, data: dict, encoding: str='ascii'):
        """ Pack, encode and send data """

        sock.send(DataPacking.pack_data(data, encoding))


class FormAlertOrError:
    """ Create json format alert/error.
    Have some texts for codes, see ALERTS_MSGS in configure.

    """

    def alerts_msg_text_from_code(self, response_code: int) -> str:
        """ Take text from number of error code.
        Take text from ALERTS_MSGS in configure.

        """

        for code, msg in ALERTS_MSGS.items():
            if int(code) == response_code:
                return msg

        return

    def form_alert_or_error(self, response_code: int,
                            text_msg_code: str = None) -> dict:
        """ Forming dict with alert/error """

        alert = 'alert'

        if response_code > 399:
            alert = 'error'

        if text_msg_code is None:
            text_msg_code: str = self.alerts_msg_text_from_code(
                response_code)

        return {
            "response": response_code, "time": int(datetime.now().timestamp()),
            alert: text_msg_code
            }
