def solution():
    """Ursula earns $8.50 an hour working in a restaurant. She works 8 hours a day. If she works 20 days a month, determine her annual salary."""
    hourly_salary = 8.5
    daily_hours = 8
    work_days_per_month = 20
    monthly_salary = hourly_salary * daily_hours * work_days_per_month
    annual_salary = monthly_salary * 12
    result = annual_salary
    return result

print(solution())