def solution():
    
    normal_apples_per_day = 40 * 50
    normal_week_total = normal_apples_per_day * 7
    reduced_apples_per_day = (40 - (500/50)) * 50
    reduced_week_total = reduced_apples_per_day * 7
    total_apples_packed = normal_week_total + reduced_week_total
    result = total_apples_packed
    return result

print(solution())