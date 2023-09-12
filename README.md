# Gm-Automation-IOS

This suite of scripts automates the sending of "good morning" messages via iMessage on macOS. The system is structured as follows:

gm_scheduler.py: Chooses a random time from the list of specified times for the next message sending and schedules the runner.
runner.py: Waits until the specified time, then triggers the message sending script.
send_gm.py: Sends a random "good morning" message from the predefined list using AppleScript.
send_imessage.scpt: An AppleScript to send an iMessage.

## Setup
1. Replace YOUR_USER and YOUR_DIRECTORY placeholders in all the scripts with appropriate paths.
2. Ensure you have Python3 installed and accessible at /usr/local/bin/python3.
3. Place the com.YOUR_USER_gmscheduler.plist into the ~/Library/LaunchAgents/ directory.

## Usage
The system utilizes macOS's launchd for scheduling. The gm_scheduler.py script is set to run at 12:12am daily, but you can adjust this as needed in the plist file.

# Launch Agent Control

## Prerequisites
Operating System: macOS

## Unloading the Agent
If you want to temporarily stop the agent from running, you can unload it. Here's how:

1. Open the Terminal.
2. Navigate to the LaunchAgents directory:
   cd ~/Library/LaunchAgents
3. Unload the agent using the launchctl command:
   launchctl unload ~/Library/LaunchAgents/com.YOUR_USER.gmscheduler.plist

## Reloading the Agent
In case you've unloaded the agent and wish to reload it:

1. Open the Terminal.
2. Navigate to the LaunchAgents directory:
   cd ~/Library/LaunchAgents
3. Reload the agent using the launchctl command:
   launchctl load ~/Library/LaunchAgents/com.YOUR_USER.gmscheduler.plist

## Confirm Agent Status
To confirm that your agent is currently loaded:

launchctl list | grep com.YOUR_USER

If the agent is loaded, this command will return its identifier (com.YOUR_USER.gmscheduler). If not, there won't be any output.

## Important Note
For the automation to work correctly, iMessage must always be open and running on the machine. Ensure you have iMessage set up and signed in, and keep it running for seamless automation.

Please make sure to replace the YOUR_USER placeholders with the appropriate values.





