import unittest
import json
from datetime import datetime

from common.utils import DataPacking as DP
from common.utils import FormAlertOrError as FAOE

alerts_msg_text_from_code = FAOE().alerts_msg_text_from_code
form_alert_or_error = FAOE().form_alert_or_error
pack_data = DP.pack_data
unpack_data = DP.unpack_data


class TestPackData(unittest.TestCase):

    def test_data(self):
        data = {
            "action": "msg",
            "time": int(datetime.now().timestamp()),
            "to": 'test',
            "from": 'msg_from',
            "encoding": 'encoding',
            "message": 'msg'
            }
        encoding = 'ascii'

        self.assertEqual(
            pack_data(data, encoding),
            json.dumps(data).encode(encoding)
            )

    def test_encoding(self):
        data = {
            "action": "msg",
            "time": int(datetime.now().timestamp()),
            "to": 'test',
            "from": 'msg_from',
            "encoding": 'encoding',
            "message": 'msg'
            }

        encodings = ('ascii', 'utf-8')

        for encoding in encodings:
            self.assertEqual(
                pack_data(data, encoding),
                json.dumps(data).encode(encoding)
                )


class TestUnpackData(unittest.TestCase):

    def test_data(self):
        data = b'{"action": "msg", "time": 1573913065, "to": "test", ' \
            b'"from": "msg_from", "encoding": "encoding", "message": "msg"}'

        encoding = 'ascii'

        self.assertEqual(
            unpack_data(data, encoding),
            json.loads(data.decode(encoding))
            )

    def test_encoding(self):
        data = b'{"action": "msg", "time": 1573913065, "to": "test", ' \
            b'"from": "msg_from", "encoding": "encoding", "message": "msg"}'

        encodings = ('ascii', 'utf-8')

        for encoding in encodings:
            self.assertEqual(
                unpack_data(data, encoding),
                json.loads(data.decode(encoding))
                )


class TestOwnAlertOrError(unittest.TestCase):

    def test_alert(self):
        msg = {
            "response": 205,
            "time": int(datetime.now().timestamp()),
            'alert': 'reset content'
            }

        self.assertEqual(form_alert_or_error(205, 'reset content'), msg)

    def test_error(self):
        msg = {
            "response": 408,
            "time": int(datetime.now().timestamp()),
            'error': 'request timeout'
            }

        self.assertEqual(form_alert_or_error(408, 'request timeout'), msg)

    def test_alert_without_text_msg_code(self):
        msg = {
            "response": 205,
            "time": int(datetime.now().timestamp()),
            'alert': None
            }

        self.assertEqual(form_alert_or_error(205), msg)

    def test_error_without_text_msg_code(self):
        msg = {
            "response": 408,
            "time": int(datetime.now().timestamp()),
            'error': None
            }

        self.assertEqual(form_alert_or_error(408), msg)


class TestTextFromCode(unittest.TestCase):

    def test_100(self):
        self.assertEqual(alerts_msg_text_from_code(100),
                         'base notification')

    def test_101(self):
        self.assertEqual(alerts_msg_text_from_code(101),
                         'important notification'
                         )

    def test_200(self):
        self.assertEqual(alerts_msg_text_from_code(200), 'OK')

    def test_201(self):
        self.assertEqual(alerts_msg_text_from_code(201), 'created')

    def test_202(self):
        self.assertEqual(alerts_msg_text_from_code(202), 'accepted')

    def test_400(self):
        self.assertEqual(alerts_msg_text_from_code(400),
                         'wrong request/JSON object'
                         )

    def test_401(self):
        self.assertEqual(alerts_msg_text_from_code(401), 'not authorized')

    def test_402(self):
        self.assertEqual(alerts_msg_text_from_code(402),
                         'wrong password or no account with that name'
                         )

    def test_403(self):
        self.assertEqual(alerts_msg_text_from_code(403), 'forbidden')

    def test_404(self):
        self.assertEqual(alerts_msg_text_from_code(404),
                         'not found chat or user'
                         )

    def test_409(self):
        self.assertEqual(alerts_msg_text_from_code(409),
                         'conflict with another one connect'
                         )

    def test_410(self):
        self.assertEqual(alerts_msg_text_from_code(410), 'gone offline')

    def test_500(self):
        self.assertEqual(alerts_msg_text_from_code(500), 'server error')


class TestFormAlert(unittest.TestCase):

    def test_100(self):
        msg = {
            "response": 100,
            "time": int(datetime.now().timestamp()),
            'alert': 'base notification'
            }

        self.assertEqual(form_alert_or_error(100), msg)

    def test_101(self):
        msg = {
            "response": 101,
            "time": int(datetime.now().timestamp()),
            'alert': 'important notification'
            }

        self.assertEqual(form_alert_or_error(101), msg)

    def test_200(self):
        msg = {
            "response": 200,
            "time": int(datetime.now().timestamp()),
            'alert': 'OK'
            }

        self.assertEqual(form_alert_or_error(200), msg)

    def test_201(self):
        msg = {
            "response": 201,
            "time": int(datetime.now().timestamp()),
            'alert': 'created'
            }

        self.assertEqual(form_alert_or_error(201), msg)

    def test_202(self):
        msg = {
            "response": 202,
            "time": int(datetime.now().timestamp()),
            'alert': 'accepted'
            }

        self.assertEqual(form_alert_or_error(202), msg)

    def test_400(self):
        msg = {
            "response": 400,
            "time": int(datetime.now().timestamp()),
            'error': 'wrong request/JSON object'
            }

        self.assertEqual(form_alert_or_error(400),  msg)

    def test_401(self):
        msg = {
            "response": 401,
            "time": int(datetime.now().timestamp()),
            'error': 'not authorized'
            }

        self.assertEqual(form_alert_or_error(401), msg)

    def test_402(self):
        msg = {
            "response": 402,
            "time": int(datetime.now().timestamp()),
            'error': 'wrong password or no account with that name'
            }

        self.assertEqual(form_alert_or_error(402), msg)

    def test_403(self):
        msg = {
            "response": 403,
            "time": int(datetime.now().timestamp()),
            'error': 'forbidden'
            }

        self.assertEqual(form_alert_or_error(403), msg)

    def test_404(self):
        msg = {
            "response": 404,
            "time": int(datetime.now().timestamp()),
            'error': 'not found chat or user'
            }

        self.assertEqual(form_alert_or_error(404), msg)

    def test_409(self):
        msg = {
            "response": 409,
            "time": int(datetime.now().timestamp()),
            'error': 'conflict with another one connect'
            }

        self.assertEqual(form_alert_or_error(409), msg)

    def test_410(self):
        msg = {
            "response": 410,
            "time": int(datetime.now().timestamp()),
            'error': 'gone offline'
            }

        self.assertEqual(form_alert_or_error(410), msg)

    def test_500(self):
        msg = {
            "response": 500,
            "time": int(datetime.now().timestamp()),
            'error': 'server error'
            }

        self.assertEqual(form_alert_or_error(500), msg)


if __name__ == '__main__':
    unittest.main()
