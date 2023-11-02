def solution():
    
    grapes_per_six_months = 90
    increase_percent = 20
    grapes_per_year = grapes_per_six_months * 2 * (1 + (increase_percent / 100))
    result = grapes_per_year
    return result

print(solution())