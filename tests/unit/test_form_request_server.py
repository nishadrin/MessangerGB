import unittest
from datetime import datetime

from common.form_request_server import is_user_online


class TestServerFormRequest(unittest.TestCase):

    def test_is_user_online(self):
        msg = {
            "action": "probe",
            "time": int(datetime.now().timestamp()),
            }

        self.assertEqual(is_user_online(), msg)


if __name__ == '__main__':
    unittest.main()
