def solution():
    
    yesterday_drinks = 48
    decrease_percentage = 4
    two_days_ago_drinks = yesterday_drinks / (1 - decrease_percentage / 100)
    result = two_days_ago_drinks
    return result

print(solution())