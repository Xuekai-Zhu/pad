def solution():
    kids_cost = 3
    adults_cost = 2 * kids_cost

    daily_income = 8 * kids_cost + 10 * adults_cost
    weekly_income = 7 * daily_income

    result = weekly_income
    return result

print(solution())