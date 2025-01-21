from telethon.sync import TelegramClient

api_id = '19948851'
api_hash = '0e3ff31968c70c1cf68384697e7a64ca'
phone_number = '+79659353352'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the code: '))
    
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        client.delete_dialog(dialog.id)
