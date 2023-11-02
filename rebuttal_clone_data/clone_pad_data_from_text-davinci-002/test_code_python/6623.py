def solution():
    tractor_rate = 75
    shovel_rate = 10
    pounds_to_load = 2550
    minutes_to_load = pounds_to_load / (tractor_rate + shovel_rate)
    result = minutes_to_load
    return result

print(solution())