def solution():
    
    total_cost = 400
    madeline_monthly_cost = total_cost * 0.6
    keenan_monthly_cost = total_cost - madeline_monthly_cost
    keenan_weekly_cost = keenan_monthly_cost / 4
    result = keenan_weekly_cost
    return result

print(solution())