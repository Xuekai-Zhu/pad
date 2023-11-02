def solution():
    messages = 98  # total number of unread messages
    messages_read_per_day = 20  # number of messages Marie reads per day
    new_messages_per_day = 6  # number of new messages Marie gets per day

    days_to_read_all_messages = (messages / messages_read_per_day) + (messages % messages_read_per_day / (messages_read_per_day - new_messages_per_day))

    result = days_to_read_all_messages
    return result

print(solution())