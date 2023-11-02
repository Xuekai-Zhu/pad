def solution():
    initial_ipods = 14
    lost_ipods = 6
    remaining_ipods = initial_ipods - lost_ipods
    rosa_ipods = remaining_ipods / 2
    total_ipods = remaining_ipods + rosa_ipods
    result = total_ipods
    return result

print(solution())