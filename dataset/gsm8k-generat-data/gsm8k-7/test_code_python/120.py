def solution():
    hourly_wage = 8
    hours_per_week = 35
    weeks_per_month = 4
    monthly_income = hourly_wage * hours_per_week * weeks_per_month
    bike_cost = 400
    money_left = monthly_income - bike_cost
    result = money_left
    return result

print(solution())