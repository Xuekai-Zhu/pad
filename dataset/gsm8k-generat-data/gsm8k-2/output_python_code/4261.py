def solution():
    """Barry and his friend, Jim, went horseback riding across central Texas. They traveled at 5 miles per hour for 7 hours, and then stopped for the evening. The next day, they traveled at 6 miles per hour for 6 hours, and then at half that speed for another three hours, before stopping to rest for the night. On the third and final day, they traveled for 5 hours at 7 miles per hour. In total, how far did they travel, in miles, during their horseback riding trip?"""
    day1_speed = 5
    day1_hours = 7
    day2_speed = 6
    day2_hours = 6
    day2_slow_speed = 0.5 * day2_speed
    day2_slow_hours = 3
    day3_speed = 7
    day3_hours = 5
    total_distance = (day1_speed * day1_hours) + (day2_speed * day2_hours) + (day2_slow_speed * day2_slow_hours) + (day3_speed * day3_hours)
    result = total_distance
    return result

print(solution())