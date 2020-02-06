import unittest
from datetime import datetime

from common.form_request_client import client_message, presence_msg, auth, \
    join_or_leave_chat


class TestClientFormRequest(unittest.TestCase):

    def test_client_message_with_encodings(self):
        encodings = ('ascii', 'utf-8')

        for encoding in encodings:
            test_msg = {
                "action": "msg",
                "time": int(datetime.now().timestamp()),
                "to": 'msg_to',
                "from": 'msg_from',
                "msg": 'msg',
                "encoding": encoding
                }

            self.assertEqual(
                client_message('msg_to', 'msg_from', 'msg', encoding=encoding),
                test_msg
                )

    def test_presence_msg(self):
        msg = {
            "action": "presence",
            "time": int(datetime.now().timestamp()),
            "type": 'type',
            "user": {
                "account_name": 'user_name',
                "status": 'status'
                }
            }

        self.assertEqual(presence_msg('user_name', 'type', 'status'), msg)

    def test_auth(self):
        msg = {
            "action": "authenticate",
            "time": int(datetime.now().timestamp()),
            "type": 'type',
            "user": {
                "account_name": 'user_name',
                "password": 'password'
                }
            }

        self.assertEqual(auth('user_name', 'password', 'type'), msg)

    def test_join_chat(self):
        msg = {
            "action": 'join',
            "time": int(datetime.now().timestamp()),
            "room": 'room_name'
            }

        self.assertEqual(join_or_leave_chat('room_name'), msg)

    def test_leave_chat(self):
        msg = {
            "action": 'leave',
            "time": int(datetime.now().timestamp()),
            "room": 'room_name'
            }

        self.assertEqual(join_or_leave_chat('room_name', True), msg)


if __name__ == '__main__':
    unittest.main()
