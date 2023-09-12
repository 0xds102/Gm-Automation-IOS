# Gm-Automation-IOS

This suite of scripts automates the sending of "good morning" messages via iMessage on macOS. The system is structured as follows:

gm_scheduler.py: Chooses a random time from the list of specified times for the next message sending and schedules the runner.
runner.py: Waits until the specified time, then triggers the message sending script.
send_gm.py: Sends a random "good morning" message from the predefined list using AppleScript.
send_imessage.scpt: An AppleScript to send an iMessage.
