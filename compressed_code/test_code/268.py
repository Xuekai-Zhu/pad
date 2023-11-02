def solution():
    
    total_tubs = 9
    total_cost = 48
    large_tub_cost = 6
    large_tub_count = 3
    total_large_tub_cost = large_tub_count * large_tub_cost
    small_tub_cost = (total_cost - total_large_tub_cost) / (total_tubs - large_tub_count)
    result = small_tub_cost
    return result

print(solution())