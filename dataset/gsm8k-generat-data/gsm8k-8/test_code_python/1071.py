def solution():
    freestyle_time = 48
    backstroke_time = freestyle_time + 4
    butterfly_time = backstroke_time + 3
    breaststroke_time = butterfly_time + 2

    total_time = freestyle_time + backstroke_time + butterfly_time + breaststroke_time
    result = total_time
    return result

print(solution())