def solution():
    hourly_rate = 8
    weekly_hours = 35
    weeks_per_month = 4
    total_earnings = hourly_rate * weekly_hours * weeks_per_month

    bike_cost = 400
    remaining_money = total_earnings - bike_cost

    result = remaining_money
    return result

print(solution())