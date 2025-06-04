import mcrcon
import subjection

print("data: 26.70.9.233", subjection.account_password, int(subjection.debug_port))
RCON_IP = "26.70.9.233"
RCON_PASSWORD = subjection.account_password
RCON_PORT = int(subjection.debug_port)
try:
    rcon = mcrcon.MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT)
    rcon.connect()
    print("✅ Успешное подключение к RCON!")

    # Чтение файла и отправка сообщений в чат
    with open("telegram_chat_log.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():  # Пропускаем пустые строки
                rcon.command(f"say {line.strip()}")
                print(f"Отправлено: {line.strip()}")

    rcon.disconnect()
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")


#python D:\projects\VisualStudioCode\TGBotPrint\send_text.py