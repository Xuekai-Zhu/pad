def solution():
    """Keiko sent 111 text messages last week. This week she sent 50 less than double what she sent last week. How many text messages did Keiko send last week and this week combined?"""
    # Define the number of text messages sent last week
    last_week_messages = 111

    # Calculate the number of text messages sent this week
    this_week_messages = 2 * last_week_messages - 50

    # Calculate the total number of messages sent
    total_messages = last_week_messages + this_week_messages

    result = total_messages
    return result

print(solution())