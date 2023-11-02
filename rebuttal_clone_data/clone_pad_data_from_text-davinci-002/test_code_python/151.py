def solution():
    """Keiko sent 111 text messages last week. This week she sent 50 less than double what she sent last week. How many text messages did Keiko sent last week and this week combined?"""
    text_messages_last_week = 111
    text_messages_this_week = (text_messages_last_week * 2) - 50
    total_text_messages = text_messages_last_week + text_messages_this_week
    result = total_text_messages
    return result

print(solution())