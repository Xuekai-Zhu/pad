def solution():
    """Barry and his friend, Jim, went horseback riding across central Texas. They traveled at 5 miles per hour for 7 hours, and then stopped for the evening. The next day, they traveled at 6 miles per hour for 6 hours, and then at half that speed for another three hours, before stopping to rest for the night. On the third and final day, they traveled for 5 hours at 7 miles per hour. In total, how far did they travel, in miles, during their horseback riding trip?"""
    day_one_speed = 5
    day_one_hours = 7
    day_two_first_speed = 6
    day_two_first_hours = 6
    day_two_second_speed = day_two_first_speed / 2
    day_two_second_hours = 3
    day_three_speed = 7
    day_three_hours = 5
    total_distance = (day_one_speed * day_one_hours) + (day_two_first_speed * day_two_first_hours) + (day_two_second_speed * day_two_second_hours) + (day_three_speed * day_three_hours)
    result = total_distance
    return result

print(solution())