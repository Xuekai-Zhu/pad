def solution():
    daily_salary = 10  # Ludwig's daily salary is $10
    full_days = 4  # Ludwig works full days from Monday to Thursday
    half_days = 1.5  # Ludwig works half of the day on Friday, Saturday, and Sunday
    total_days = 7  # Ludwig works 7 days a week

    # Calculate Ludwig's weekly earnings
    weekly_earnings = (full_days * daily_salary * 4) + (half_days * daily_salary * 3)

    result = weekly_earnings
    return result

print(solution())