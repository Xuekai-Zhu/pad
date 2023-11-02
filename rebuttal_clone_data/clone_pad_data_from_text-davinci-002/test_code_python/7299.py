def solution():
    leaves = 340
    leaves_lost_per_day = 0.1 * leaves
    total_leaves_lost = leaves_lost_per_day * 4
    leaves_left = leaves - total_leaves_lost
    leaves_dropped_on_fifth_day = leaves - leaves_left
    result = leaves_dropped_on_fifth_day
    
    return result

print(solution())