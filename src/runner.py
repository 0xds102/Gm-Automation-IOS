import datetime
import time
import subprocess
import os

LOG_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/gm_logs.txt"
LAST_LOG_DAY_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/last_log_day.txt"
SCHEDULED_TIME_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/scheduled_time.txt"

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

log_message("Executing runner.py")
log_message(f"Attempting to read scheduled GM time from {os.path.basename(SCHEDULED_TIME_FILE)}")
with open(SCHEDULED_TIME_FILE, 'r') as f:
    scheduled_time_str = f.read().strip()

log_message(f"Scheduled GM time read: {scheduled_time_str}")

scheduled_hour, scheduled_minute = map(int, scheduled_time_str.split(':'))

# Calculate the seconds until the scheduled time
now = datetime.datetime.now()
scheduled_datetime = datetime.datetime(now.year, now.month, now.day, scheduled_hour, scheduled_minute)
if scheduled_datetime <= now:
    scheduled_datetime += datetime.timedelta(days=1)

seconds_until_scheduled = (scheduled_datetime - now).total_seconds()

log_message(f"Sleeping for {seconds_until_scheduled} seconds until scheduled GM time")

time.sleep(seconds_until_scheduled)

log_message("Waking up to execute send_gm.py")

try:
    subprocess.run(["/usr/local/bin/python3", "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/src/send_gm.py"])
except Exception as e:
    log_message(f"Error while running send_gm.py: {str(e)}")

log_message("runner.py completed")

