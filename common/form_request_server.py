from datetime import datetime


def is_user_online() -> dict:

    return {
        "action": "probe",
        "time": int(datetime.now().timestamp()),
        }
