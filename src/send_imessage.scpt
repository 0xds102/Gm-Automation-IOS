on run {targetBuddyPhone, targetMessage}
    with timeout of 300 seconds
        tell application "Messages"
            set targetService to 1st account whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
        end tell
    end timeout
end run
