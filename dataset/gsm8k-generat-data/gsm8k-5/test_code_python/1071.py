def solution():
    freestyle_time = 48  # David's time for 100m freestyle in seconds
    backstroke_time = freestyle_time + 4  # David's time for 100m backstroke in seconds
    butterfly_time = backstroke_time + 3  # David's time for 100m butterfly in seconds
    breaststroke_time = butterfly_time + 2  # David's time for 100m breaststroke in seconds

    # Calculate the total time for David to swim all four events
    total_time = freestyle_time + backstroke_time + butterfly_time + breaststroke_time
    result = total_time
    return result

print(solution())