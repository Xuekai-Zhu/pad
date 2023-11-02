def solution():
    terry_income = 24
    jordan_income = 30
    days_per_week = 7

    # Calculate Terry's weekly income
    terry_weekly_income = terry_income * days_per_week

    # Calculate Jordan's weekly income
    jordan_weekly_income = jordan_income * days_per_week

    # Calculate the difference between their weekly incomes
    income_difference = jordan_weekly_income - terry_weekly_income
    result = income_difference
    return result

print(solution())