def solution():
    # Define the number of hours logged per day
    daily_hours = 10

    # Define the number of days worked per week
    weekly_days = 5

    # Calculate the total hours logged in one week
    weekly_hours = daily_hours * weekly_days

    # Calculate the total hours logged in one month
    monthly_hours = weekly_hours * 4

    result = monthly_hours
    return result

print(solution())