def solution():
    base_time = 10  # seconds
    time_one = base_time * 2  # first week
    time_two = time_one * 2  # second week
    time_three = time_two * 1.5  # third week
    total_time = time_one + time_two + time_three  # total time
    result = total_time
    return result

print(solution())