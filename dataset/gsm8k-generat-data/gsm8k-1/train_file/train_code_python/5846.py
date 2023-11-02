def solution():
    """Ursula earns $8.50 an hour working in a restaurant. She works 8 hours a day. If she works 20 days a month, determine her annual salary."""
    hourly_rate = 8.5
    hours_per_day = 8
    days_per_month = 20
    days_per_year = 365
    annual_salary = hourly_rate * hours_per_day * days_per_month * 12
    result = annual_salary
    return result

print(solution())