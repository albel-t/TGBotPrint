import mcrcon
import subjection

rcon = mcrcon.MCRcon("localhost", subjection.account_password, int(subjection.debug_port))
rcon.connect()

with open("telegram_chat_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():  # Пропускаем пустые строки
            rcon.command(f"say {line.strip()}")

rcon.disconnect()