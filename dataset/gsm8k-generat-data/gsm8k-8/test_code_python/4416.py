def solution():
    daily_rate = 30
    weekly_rate = 190
    rental_period = 11

    # Check if rental qualifies for weekly rate
    if rental_period >= 7:
        weeks = rental_period // 7
        days = rental_period % 7
        total_cost = weeks * weekly_rate + days * daily_rate
    else:
        total_cost = rental_period * daily_rate

    result = total_cost
    return result

print(solution())