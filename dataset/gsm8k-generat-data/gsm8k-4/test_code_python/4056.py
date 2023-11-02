def solution():
    """Terry's daily income is $24, while Jordan's daily income is $30. Working 7 days a week, how much is the difference between their weekly incomes?"""
    # Define the daily earnings of Terry and Jordan
    terry_daily_earnings = 24
    jordan_daily_earnings = 30

    # Calculate the weekly earnings of Terry and Jordan
    terry_weekly_earnings = terry_daily_earnings * 7
    jordan_weekly_earnings = jordan_daily_earnings * 7

    # Calculate the difference in their weekly earnings
    income_difference = abs(terry_weekly_earnings - jordan_weekly_earnings)

    # return the result
    result = income_difference
    return result

print(solution())