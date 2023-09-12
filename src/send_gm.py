import random
import datetime
import subprocess
import os

LOG_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/gm_logs.txt"
LAST_LOG_DAY_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/last_log_day.txt"

gm_messages = [
    "goodmorning",
    "gm",
    "YOUR_CUSTOM_GM_MESSAGES"
]

def log_message(msg):
    current_day = datetime.datetime.now().date()

    if not os.path.exists(LAST_LOG_DAY_FILE) or open(LAST_LOG_DAY_FILE, 'r').read().strip() != str(current_day):
        with open(LAST_LOG_DAY_FILE, 'w') as f:
            f.write(str(current_day))
        
        with open(LOG_FILE, 'a') as f:
            f.write("\n-----------------------------------\n")
            f.write(f"Logs for {current_day}\n")
            f.write("-----------------------------------\n")

    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()} - {msg}\n")

def send_message(phone_number, message):
    result = subprocess.run(
        ["/usr/bin/osascript", "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/src/send_imessage.scpt", phone_number, message],
        capture_output=True,
        text=True
    )
    if result.stderr:
        log_message(f"Subprocess error: {result.stderr}")
    else:
        log_message(f"Message '{message}' ₿$$₿__delivered_₿$$₿")

if __name__ == "__main__":
    log_message("Executing send_gm.py")
    send_message("+_YOUR_NUMBER", random.choice(gm_messages))
    log_message("send_gm.py completed")
