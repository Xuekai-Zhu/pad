def solution():
    
    apple_pies_per_day = 12
    cherry_pies_per_day = 12
    days_per_week = 5
    apple_pies_per_week = apple_pies_per_day * 3
    cherry_pies_per_week = cherry_pies_per_day * 2
    more_apple_pies = apple_pies_per_week - cherry_pies_per_week
    result = more_apple_pies
    return result

print(solution())