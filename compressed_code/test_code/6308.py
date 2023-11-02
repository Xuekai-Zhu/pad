def solution():
    
    total_savings_goal = 150
    savings_per_month_jan_to_jul = 10
    savings_per_month_aug_to_nov = 15
    savings_jan_to_jul = savings_per_month_jan_to_jul * 7
    savings_aug_to_nov = savings_per_month_aug_to_nov * 4
    total_savings_jan_to_nov = savings_jan_to_jul + savings_aug_to_nov
    savings_dec = total_savings_goal - total_savings_jan_to_nov
    result = savings_dec
    return result

print(solution())