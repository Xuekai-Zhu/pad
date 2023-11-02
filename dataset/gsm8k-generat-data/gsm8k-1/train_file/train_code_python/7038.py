def solution():
    """Jerry can run from his house to his school and back in the time it takes his brother Carson to run to the school.
    If it takes Jerry 15 minutes to make a one-way trip from his house to his school and the school is 4 miles away,
    how fast does Carson run in miles per hour?"""
    distance = 4
    jerry_time = 0.5 # 15 minutes = 0.5 hours
    carson_time = jerry_time / 2
    carson_speed = distance / carson_time
    result = carson_speed
    return result

print(solution())