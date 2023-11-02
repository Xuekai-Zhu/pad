def solution():
    """Jerry can run from his house to his school and back in the time it takes his brother Carson to run to the school. If it takes Jerry 15 minutes to make a one-way trip from his house to his school and the school is 4 miles away, how fast does Carson run in miles per hour?"""
    # Define the distance and time for Jerry's one-way trip
    jerry_distance = 4
    jerry_time = 0.25 # 15 minutes = 0.25 hours

    # Calculate the round-trip distance and time for Jerry
    jerry_round_distance = jerry_distance * 2
    jerry_round_time = jerry_time * 2

    # Calculate the time it takes Carson to run to the school
    carson_time = jerry_round_time / 2

    # Calculate Carson's speed in miles per hour
    carson_speed = jerry_round_distance / carson_time

    # Display Carson's speed
    result = carson_speed
    return result

print(solution())