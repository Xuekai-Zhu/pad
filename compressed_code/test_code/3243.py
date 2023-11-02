def solution():
    
    first_day = 2
    second_day = first_day * 2
    third_day = second_day * 2
    sandwiches_per_cycle = first_day + second_day + third_day
    cycles = 6 // 3
    total_sandwiches = cycles * sandwiches_per_cycle
    remaining_days = 6 % 3
    if remaining_days == 1:
        total_sandwiches += first_day
    elif remaining_days == 2:
        total_sandwiches += first_day + second_day
    result = total_sandwiches
    return result

print(solution())