from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Замените на свои данные, полученные на https://my.telegram.org
api_id = 29180707  # <-- Сюда вставь свой API ID
api_hash = 'eef15de3dd82c3774f5d8985bf9f0c58'  # <-- Сюда вставь свой API HASH

print("Добро пожаловать в Telegram-регистрацию 🎉")
phone = input("Введите ваш номер телефона (например, +79991234567): ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    # Отправка кода на телефон
    client.send_code_request(phone)
    code = input("Введите код из Telegram: ")

    try:
        client.sign_in(phone, code)
    except Exception as e:
        print("Возможно, включена двухфакторная аутентификация.")
        password = input("Введите пароль: ")
        client.sign_in(password=password)

    print("✅ Успешная регистрация или вход!")

    # Отправка сообщения самому себе — подарок
    me = client.get_me()
    message = "🎁 Поздравляем! Вы получили подарок за регистрацию! 🎉"
    client.send_message(me.username or me.id, message)
    print("🎉 Подарок отправлен в ваш Telegram!")
