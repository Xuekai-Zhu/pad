def solution():
    """Jerry can run from his house to his school and back in the time it takes his brother Carson to run to the school. If it takes Jerry 15 minutes to make a one-way trip from his house to his school and the school is 4 miles away, how fast does Carson run in miles per hour?"""
    jerry_distance = 4 * 2 # round-trip distance
    jerry_time = 15 * 2 # round-trip time in minutes
    jerry_speed = jerry_distance / (jerry_time / 60) # convert time to hours

    carson_distance = 4 # one-way distance
    carson_time = (jerry_time / 2) / 60 # convert time to hours, assume Carson runs the same speed as Jerry for one-way
    carson_speed = carson_distance / carson_time

    result = carson_speed
    return result

print(solution())