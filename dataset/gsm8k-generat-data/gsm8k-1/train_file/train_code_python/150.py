def solution():
    """Keiko sent 111 text messages last week. This week she sent 50 less than double what she sent last week. How many text messages did Keiko send last week and this week combined?"""
    last_week = 111
    this_week = (2 * last_week) - 50
    total_messages = last_week + this_week
    result = total_messages
    return result

print(solution())