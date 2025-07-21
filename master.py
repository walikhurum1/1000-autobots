import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

BOTS_FOLDER = "/opt/1000-autobots/bots"
LOG_FOLDER = "/opt/1000-autobots/logs"

os.makedirs(LOG_FOLDER, exist_ok=True)

for filename in os.listdir(BOTS_FOLDER):
    if filename.endswith(".py") and filename.startswith("bot-"):
        bot_path = os.path.join(BOTS_FOLDER, filename)
        log_path = os.path.join(LOG_FOLDER, f"{filename}.log")

        print(f"[+] Launching {filename}...")

        with open(log_path, "a") as log_file:
            subprocess.Popen(
                ["python3", bot_path],
                stdout=log_file,
                stderr=log_file,
                text=True,
            )
