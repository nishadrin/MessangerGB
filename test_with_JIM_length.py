from common.client.form_request import client_message
from common.utils import DataPacking as DP
from common.config import JIM_MAX_BYTES


pack_data = DP.pack_data


msg_to = '1234567890123456789012345' # 25 символов
msg_from = '1234567890123456789012346' # 25 символов
msg = 'б' * 83 # 500- символов

jim_msg_lenght = len(pack_data(client_message(msg_to, msg_from, msg, encoding='utf-8'),
        encoding='ascii'))

print('Длина передаваемого сообщения:', jim_msg_lenght)

if jim_msg_lenght > JIM_MAX_BYTES:
    print('Сообщение не пройдет')

elif jim_msg_lenght == JIM_MAX_BYTES:
    print('Сообщение пройдет')

else:
    print('Сообщение пройдет')

# проведя небольшие исследования, пришел к выводу, что в
# form_request.client_message необходимо изменить название сообщений на
# msg, вместо message, тогда можем себе позволить 499 символов на
# само сообщение, поддерживающее русский язык - 83
