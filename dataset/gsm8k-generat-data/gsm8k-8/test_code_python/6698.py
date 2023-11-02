def solution():
    # Define the initial number of unread messages and the amount she can read and receive each day
    unread_messages = 98
    messages_per_day = 20
    new_messages_per_day = 6

    # Calculate the number of days it will take to read all the messages
    days_to_clear = (unread_messages / messages_per_day) + ((unread_messages % messages_per_day + new_messages_per_day) / messages_per_day)
    result = days_to_clear
    return result

print(solution())