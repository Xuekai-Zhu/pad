def solution():
    daily_rate = 30
    weekly_rate = 190
    rental_days = 11
    # If rental is more than a week, use weekly rate
    if rental_days >= 7:
        total_cost = weekly_rate + daily_rate * (rental_days - 7)
    else:
        total_cost = daily_rate * rental_days

    result = total_cost
    return result

print(solution())