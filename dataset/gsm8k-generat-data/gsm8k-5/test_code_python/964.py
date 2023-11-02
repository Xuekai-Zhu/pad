def solution():
    Kevin_ate = 64  # Kevin holds the record for eating 64 hot wings in 8 minutes
    Kevin_speed = Kevin_ate / 8  # Kevin ate 64 wings in 8 minutes, so his speed is 8 wings per minute

    Alan_speed = 5  # Alan is currently able to eat 5 wings per minute
    Alan_time = Kevin_ate / Alan_speed  # It will take Alan this many minutes to eat 64 wings
    Alan_goal_speed = Kevin_ate / 8 / Alan_time  # To beat Kevin's record, Alan needs to eat this many wings per minute

    # Calculate the difference between Alan's current speed and his goal speed
    difference = Alan_goal_speed - Alan_speed
    result = difference
    return result

print(solution())