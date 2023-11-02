def solution():
    unread_messages = 98  # Marie has 98 unread messages
    messages_per_day = 20  # Marie reads 20 messages per day
    new_messages_per_day = 6  # Marie gets 6 new messages per day

    # Calculate the number of days needed to clear all unread messages
    days = (unread_messages / messages_per_day) + ((unread_messages % messages_per_day + new_messages_per_day) / messages_per_day)

    result = days 
    return result

print(solution())