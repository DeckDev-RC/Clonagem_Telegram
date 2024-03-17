from telethon import TelegramClient, sync
from time import sleep
import requests
from senhas import api_hash, api_id

sessao = 'Repassar M'

client = TelegramClient(sessao, api_id, api_hash)
client.start()

dialogs = client.get_dialogs()
for dialog in dialogs:
    print('--------------------------------')
    if dialog.id < 0:
        print(f'Grupo: {dialog.title}')
        print(f'id: {dialog.id}')
    else:
        print(f'Nome: {dialog.title}')
        print(f'id: {dialog.id}')
    print('--------------------------------\n')
client.disconnect()
