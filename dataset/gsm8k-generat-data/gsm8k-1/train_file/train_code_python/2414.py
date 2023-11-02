def solution():
    """There were some snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. If there were 58 snowflakes after 1 hour, how many snowflakes were there at first?"""
    snowflakes_per_5_minutes = 4
    hours = 1
    total_time_in_5_minutes = (hours * 60) // 5
    total_snowflakes = 58
    snowflakes_at_first = total_snowflakes - (snowflakes_per_5_minutes * total_time_in_5_minutes)
    result = snowflakes_at_first
    return result

print(solution())