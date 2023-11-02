def solution():
    
    initial_value = 100
    six_month_drop = 0.25
    one_year_drop = 0.2
    value_after_six_months = initial_value * (1 - six_month_drop)
    value_after_one_year = value_after_six_months * (1 - one_year_drop)
    result = value_after_one_year
    return result

print(solution())