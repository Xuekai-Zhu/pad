def solution():
    messages_last_week = 111  # Keiko sent 111 messages last week
    messages_this_week = (2 * messages_last_week) - 50  # Keiko sent 50 less than double what she sent last week

    # Calculate the total number of messages Keiko sent
    total_messages = messages_last_week + messages_this_week
    result = total_messages
    return result

print(solution())