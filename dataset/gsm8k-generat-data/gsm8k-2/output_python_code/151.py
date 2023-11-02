def solution():
    """Keiko sent 111 text messages last week. This week she sent 50 less than double what she sent last week. How many text messages did Keiko send last week and this week combined?"""
    last_week_msgs = 111
    this_week_msgs = (2 * last_week_msgs) - 50
    total_msgs = last_week_msgs + this_week_msgs
    result = total_msgs
    return result

print(solution())