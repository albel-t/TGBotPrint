import mcrcon

rcon = mcrcon.MCRcon("localhost", "$BS#4xMgaFqH@7y", 25575)
rcon.connect()

with open("telegram_chat_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():  # Пропускаем пустые строки
            rcon.command(f"say {line.strip()}")

rcon.disconnect()