def solution():
    
    base_recess_time = 20
    extra_time_per_A = 2
    extra_time_per_B = 1
    less_time_per_D = 1
    total_extra_time = (10 * extra_time_per_A) + (12 * extra_time_per_B) - (5 * less_time_per_D)
    total_recess_time = base_recess_time + total_extra_time
    result = total_recess_time
    return result

print(solution())