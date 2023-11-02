def solution():
    
    rental_length = 11
    weekly_rate = 190
    daily_rate = 30
    if rental_length >= 7:
        total_cost = weekly_rate + daily_rate * (rental_length - 7)
    else:
        total_cost = daily_rate * rental_length
    result = total_cost
    return result

print(solution())