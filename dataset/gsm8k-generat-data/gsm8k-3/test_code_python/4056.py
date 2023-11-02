def solution():
    """Terry's daily income is $24, while Jordan's daily income is $30. Working 7 days a week, how much is the difference between their weekly incomes?"""
    # Define Terry's daily income and number of days worked
    TERRY_DAILY_INCOME = 24
    DAYS_WORKED = 7

    # Define Jordan's daily income and number of days worked
    JORDAN_DAILY_INCOME = 30
    DAYS_WORKED = 7

    # Calculate Terry's weekly income
    terry_weekly_income = TERRY_DAILY_INCOME * DAYS_WORKED

    # Calculate Jordan's weekly income
    jordan_weekly_income = JORDAN_DAILY_INCOME * DAYS_WORKED

    # Calculate the difference between their weekly incomes
    income_difference = jordan_weekly_income - terry_weekly_income

    # Display the income difference
    result = income_difference
    return result

print(solution())