from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel

from senhas import api_hash, api_id
import re

sessao = 'Dog 2.0'

client = TelegramClient(sessao, api_id, api_hash)

teste = 1001599946015
meu_canal = 1002033024094

substituicoes = {
    'LUCRO': 'AAAAAAAA',
}
client.start(bot_token=None)


@client.on(events.NewMessage(chats=teste))
async def pegando_mensagens(event):
    print("Received a new message.")
    try:
        my_channel = await client.get_entity(meu_canal)
        print("Channel entity found:", my_channel)
    except Exception as e:
        print("Error:", e)
    if event.text:
        text = event.text
        # Use uma expressão regular para encontrar URLs em mensagens
       # urls = re.findall(
       #     r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

        # Substitua cada URL encontrada pela string 'URL_SUBSTITUIDA'
       # for url in urls:
       #     text = text.replace(url, '.')

        # Expressão que encontra palavras que começam com "@"
        text = re.sub(r'@\w+', '@Brando', text)

        for palavra, substituicao in substituicoes.items():
            text = text.replace(palavra, substituicao)

        # Adicione o texto desejado ao final da mensagem
        texto_adicional = '@BRANDO'
        # Use '\n' para adicionar uma nova linha antes do texto adicional
        text += "\n" + texto_adicional

        if event.media:
            # Se a mensagem contém mídia, mantenha a mídia e adicione o texto modificado
            await client.send_message(text, file=event.media)
        else:
            # Se não há mídia, envie apenas o texto modificado
            await client.send_message(text)

client.start()
client.run_until_disconnected()
