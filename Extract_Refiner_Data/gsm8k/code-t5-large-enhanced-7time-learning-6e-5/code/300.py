def solution():
    
    # Define the number of hours worked and the hourly wage
    hours_per_day = 10
    hourly_wage = 10

    # Define the number of days worked in a week
    days_per_week = 5

    # Calculate the total earnings for the week
    weekly_earnings = (hours_per_day * hourly_wage * days_per_week) + (300 * hours_per_day)

    # Calculate the total earnings for the whole month
    monthly_earnings = weekly_earnings * 4

    # return the result
    result = monthly_earnings
    return result

print(solution())