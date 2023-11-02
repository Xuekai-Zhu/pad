def solution():
    """An Italian restaurant earns $600 every weekday and twice as much on the weekend. How much money does it earn by the end of the month?"""
    weekday_income = 600 * 5
    weekend_income = 2 * (600 * 2)
    total_income = weekday_income + weekend_income
    monthly_income = total_income * 4
    result = monthly_income
    return result

print(solution())