def solution():
    normal_distance = 150
    normal_time = 3
    extra_distance = 50

    # Calculate the total distance John traveled
    total_distance = normal_distance + extra_distance

    # Calculate John's speed
    speed = total_distance / normal_time

    # Calculate the total time of John's trip, including the extra distance and time to get back on track
    total_time = normal_time + (extra_distance / speed)

    result = total_time
    return result

print(solution())