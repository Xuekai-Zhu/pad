def solution():
    miles_per_week = 50 * 3 + 100 * 4
    miles_per_year = miles_per_week * 52
    cost_per_mile = 0.1
    weekly_fee = 100

    total_cost = miles_per_year * cost_per_mile + weekly_fee * 52
    result = total_cost
    return result

print(solution())