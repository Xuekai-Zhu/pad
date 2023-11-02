def solution():
    total_time = 30  # We have 30 minutes to get to school
    travel_time = 15 + 6  # It takes us 15 minutes to get to the gate and 6 minutes to get to the building
    remaining_time = total_time - travel_time  # We have this much time left to get to our room

    result = remaining_time
    return result

print(solution())