def solution():
    
    week_1_growth = 2
    week_2_growth = 2 * week_1_growth
    week_3_growth = 4 * week_2_growth
    total_growth = week_1_growth + week_2_growth + week_3_growth
    result = total_growth
    return result

print(solution())