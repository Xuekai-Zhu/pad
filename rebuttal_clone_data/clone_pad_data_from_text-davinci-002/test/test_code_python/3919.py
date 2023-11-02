def solution():
    capacity = 4000
    fill_rate = 10
    target_level = capacity * 3/4
    time_needed = target_level / fill_rate
    result = time_needed
    return result

print(solution())