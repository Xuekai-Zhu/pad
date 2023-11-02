def solution():
    hourly_rate = 8.50  # Ursula earns $8.50 per hour
    hours_per_day = 8  # Ursula works 8 hours per day
    days_per_month = 20  # Ursula works 20 days per month

    # Calculate Ursula's monthly salary
    monthly_salary = hourly_rate * hours_per_day * days_per_month

    # Calculate Ursula's annual salary
    annual_salary = monthly_salary * 12

    result = annual_salary
    return result

print(solution())