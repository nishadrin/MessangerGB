from datetime import datetime


def client_message(
        msg_to: str, msg_from: str, msg: str, encoding: str ="ascii"
        ) -> dict:

    return {
        "action": "msg",
        "time": int(datetime.now().timestamp()),
        "to": msg_to,
        "from": msg_from,
        "msg": msg,
        "encoding": encoding
        }


def presence_msg(
        user_name: str, type: str='status', status: str="Hello world!"
        ) -> dict:

    return {
        "action": "presence",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "status": status
            }
        }


def auth(user_name: str, password: str, type: str='Status') -> dict:

    return {
        "action": "authenticate",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "password": password
            }
        }


def join_or_leave_chat(room_name, leave: bool=False) -> dict:
    action = 'join'
    if leave:
        action = 'leave'

    return {
        "action": action,
        "time": int(datetime.now().timestamp()),
        "room": room_name
        }
