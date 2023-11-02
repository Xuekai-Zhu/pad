def solution():
    initial_iPods = 14
    lost_iPods = 6
    remaining_iPods = initial_iPods - lost_iPods
    rosa_iPods = remaining_iPods / 2
    total_iPods = remaining_iPods + rosa_iPods
    result = total_iPods
    return result

print(solution())