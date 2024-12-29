import os
import subprocess

defender_path = r"C:\Program Files\Shadow Defender\Defender.exe"

with open(defender_path, "rb") as reader:
    defender_data = reader.read()

defender_data = defender_data.replace(b"\x0F\x85\x82\x00\x00\x00\xE8\x18\x6E\xFE\xFF", b"\x0F\x84\x82\x00\x00\x00\xE8\x18\x6E\xFE\xFF")

with open(defender_path, "wb") as writer:
    writer.write(defender_data)

os.system('taskkill /f /im Defender.exe')
subprocess.Popen([defender_path])