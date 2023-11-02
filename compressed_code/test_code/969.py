def solution():
    
    toothpaste_size = 105
    total_daily_usage = 3+2+1+1
    total_daily_usage_grams = total_daily_usage * 3
    days_until_empty = toothpaste_size // total_daily_usage_grams
    result = days_until_empty
    return result

print(solution())