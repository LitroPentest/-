# userbot.py
import requests
from telethon import TelegramClient, events

# Конфигурация
API_ID = 22919906
API_HASH = '1657477543d49df9a2db86a95527c284'
PHONE = '+4917616352600'

# Инициализация клиента
client = TelegramClient('userbot_session', API_ID, API_HASH)

def get_catgirl_url():
    """Получает ссылку на картинку кошкодевочки через API."""
    try:
        response = requests.get('https://nekos.best/api/v2/neko')
        data = response.json()
        return data['results'][0]['url']
    except Exception as e:
        print(f"Ошибка при запросе API: {e}")
        return None

@client.on(events.NewMessage(pattern=r'\.аниме', outgoing=True))
async def handler(event):
    """Слушает команду .аниме, удаляет её и отправляет фото."""
    # Удаляем сообщение с командой
    await event.delete()
    
    # Получаем URL фото
    img_url = get_catgirl_url()
    
    if img_url:
        # Отправляем фото
        await client.send_file(event.chat_id, img_url)
    else:
        # Если API не ответило, шлем временное сообщение об ошибке
        msg = await client.send_message(event.chat_id, "Ошибка получения фото.")
        await msg.delete() # Удаляем его через некоторое время, если хочешь

# Запуск
print("Юзербот запущен...")
client.start(phone=PHONE)
client.run_until_disconnected()