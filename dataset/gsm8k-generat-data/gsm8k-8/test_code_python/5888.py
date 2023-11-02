def solution():
    # Define the hourly rate and hours worked per day and week
    hourly_rate = 5
    daily_hours = 8
    weekly_hours = daily_hours * 6

    # Calculate the weekly salary before a missed day
    weekly_salary = hourly_rate * weekly_hours

    # Calculate the daily salary and subtract it from the weekly salary to account for the missed day
    daily_salary = hourly_rate * daily_hours
    adjusted_weekly_salary = weekly_salary - daily_salary

    # Calculate the monthly salary, assuming 4 weeks in a month
    monthly_salary = adjusted_weekly_salary * 4
    result = monthly_salary
    return result

print(solution())