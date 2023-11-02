def solution():
    kibble_rate = 1/4
    kibble_left = 1
    kibble_start = 3
    hours_away = (kibble_start - kibble_left) / kibble_rate
    result = hours_away
    return result

print(solution())