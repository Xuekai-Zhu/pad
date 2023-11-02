def solution():
    """Irene earns $500 if she works for 40 hours a week and gets an extra $20 for every hour of overtime. If she worked 50 hours last week, calculate her total income."""
    
    hourly_rate = 500
    overtime_rate = 20
    regular_hours = 40
    overtime_hours = 10
    
    total_income = (hourly_rate * regular_hours) + (overtime_rate * overtime_hours)
    return total_income

print(solution())