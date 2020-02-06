import unittest
import subprocess

from client import event_handler as EH_client
from common.config import PROJECT_MAIN_PATH


class TestEventHandler(unittest.TestCase):
    pass


class TestConnections(unittest.TestCase):
    def connection(self, process, addr, port):

        return subprocess.Popen(
            [process, addr, '--port', port],
            stdout=subprocess.PIPE,
            start_new_session=True
            )

    def event_handler_client(self):
        addr, port = DEFAULT_IP_ADDRESS, DEFAULT_SERVER_PORT
        connect_server = self.connection(
            'python3 ' + PROJECT_MAIN_PATH + 'server.py', addr, port
            )
        connect_client = self.connection(
            'python3 ' + PROJECT_MAIN_PATH + 'client.py', addr, port
            )

        EH_client(connect_client)

        self.assertIsNotNone()


if __name__ == '__main__':
    unittest.main()
