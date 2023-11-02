def solution():
    initial_weight = 6
    weight_at_9_weeks = initial_weight * 2
    weight_at_3_months = weight_at_9_weeks * 2
    weight_at_5_months = weight_at_3_months * 2
    weight_at_1_year = weight_at_5_months + 30
    result = weight_at_1_year
    
    return result

print(solution())