def solution():
    # Calculate the time taken for each event
    freestyle_time = 48
    backstroke_time = freestyle_time + 4
    butterfly_time = backstroke_time + 3
    breaststroke_time = butterfly_time + 2

    # Calculate the total time taken to swim all four events
    total_time = freestyle_time + backstroke_time + butterfly_time + breaststroke_time
    result = total_time
    return result

print(solution())