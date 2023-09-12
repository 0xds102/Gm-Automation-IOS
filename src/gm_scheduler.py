import random
import datetime
import subprocess
import os

LOG_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/gm_logs.txt"
LAST_LOG_DAY_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/last_log_day.txt"
SCHEDULED_TIME_FILE = "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/logs/scheduled_time.txt"

gm_times = ["7:01", "7:03", "7:07", "7:09", "7:11", "7:13", "7:17", "7:23", "7:33", "7:53", "7:57"]

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

def choose_and_schedule_gm_time():
    log_message("Executing gm_scheduler.py")

    chosen_gm_time_str = random.choice(gm_times)
    log_message(f"Chosen GM time for the next day: {chosen_gm_time_str}")

    # Save the chosen time for the next day to a file
    with open(SCHEDULED_TIME_FILE, 'w') as f:
        f.write(chosen_gm_time_str)

    subprocess.run(["/usr/local/bin/python3", "/Users/YOUR_USER/YOUR_DIRECTORY/gm-automation/src/runner.py"])

    log_message("gm_scheduler.py completed")

if __name__ == "__main__":
    choose_and_schedule_gm_time()
