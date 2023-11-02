def solution():
    """Irene earns $500 if she works for 40 hours a week and gets an extra $20 for every hour of overtime. If she worked 50 hours last week, calculate her total income."""
    base_salary = 500
    overtime_salary = 20
    regular_hours = 40
    overtime_hours = 50 - regular_hours
    total_salary = base_salary + (overtime_salary * overtime_hours)
    result = total_salary
    return result

print(solution())