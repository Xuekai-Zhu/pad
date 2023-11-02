def solution():
    # Set the hourly wage and daily hours worked
    hourly_wage = 8.5
    daily_hours = 8

    # Calculate the daily earnings
    daily_earnings = hourly_wage * daily_hours

    # Calculate the monthly earnings (20 work days)
    monthly_earnings = daily_earnings * 20

    # Calculate the annual earnings (12 months)
    annual_earnings = monthly_earnings * 12

    result = annual_earnings
    return result

print(solution())