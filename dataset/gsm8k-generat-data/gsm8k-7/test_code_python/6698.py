def solution():
    unread_messages = 98
    read_per_day = 20
    new_per_day = 6

    days = (unread_messages / read_per_day) + (unread_messages % read_per_day > 0) # round up
    total_new_messages = days * new_per_day
    total_messages = unread_messages + total_new_messages
    result = days
    return result

print(solution())