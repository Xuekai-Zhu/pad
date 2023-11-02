def solution():
    """Jerry can run from his house to his school and back in the time it takes his brother Carson to run to the school. If it takes Jerry 15 minutes to make a one-way trip from his house to his school and the school is 4 miles away, how fast does Carson run in miles per hour?"""
    # Calculate the round trip time for Jerry
    jerry_time = 2 * (15 / 60)  # in hours

    # Calculate the one-way time for Jerry
    jerry_one_way_time = jerry_time / 2

    # Calculate the speed of Jerry
    jerry_speed = 4 / jerry_one_way_time  # in miles per hour

    # Calculate the time it takes Carson to run to the school
    carson_time = jerry_one_way_time

    # Calculate the speed of Carson
    carson_speed = 4 / carson_time  # in miles per hour

    result = carson_speed
    return result

print(solution())