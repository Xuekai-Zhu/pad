def solution():
    barrels = 12
    minutes_to_fill = 3
    minutes_with_leak = 5
    time_saved = minutes_to_fill - minutes_with_leak
    time_needed = time_saved * barrels
    result = time_needed
    return result

print(solution())