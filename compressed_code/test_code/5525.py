def solution():
    
    normal_time_per_cake = 5
    injured_time_per_cake = 8
    extra_time_per_cake = injured_time_per_cake - normal_time_per_cake
    num_cakes = 10
    extra_time_total = extra_time_per_cake * num_cakes
    result = extra_time_total
    return result

print(solution())