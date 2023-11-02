def solution():
    num_messages_last_week = 111
    num_messages_this_week = (2 * num_messages_last_week) - 50

    # Calculate the total number of messages sent
    total_messages = num_messages_last_week + num_messages_this_week
    result = total_messages
    return result

print(solution())