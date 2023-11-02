def solution():
    
    rental_days = 11
    weekly_rate = 190
    daily_rate = 30
    if rental_days >= 7:
        total_cost = weekly_rate + ((rental_days - 7) * daily_rate)
    else:
        total_cost = rental_days * daily_rate
    result = total_cost
    return result

print(solution())