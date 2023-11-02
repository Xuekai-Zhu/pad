def solution():
    # Calculate the effective speed of Karen
    karen_speed = 10 - 4  # Karen's speed against the current is her still pond speed minus the river's speed
    river_length = 12  # the length of the river in miles
    time_to_paddle = river_length / karen_speed  # time to paddle up the river
    result = time_to_paddle
    return result

print(solution())