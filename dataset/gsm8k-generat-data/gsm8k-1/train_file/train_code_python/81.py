def solution():
    """Irene earns $500 if she works for 40 hours a week and gets an extra $20 for every hour of overtime. If she worked 50 hours last week, calculate her total income."""
    base_pay = 500
    regular_hours = 40
    overtime_rate = 20
    overtime_hours = 10
    total_pay = base_pay + ((overtime_rate * overtime_hours))
    result = total_pay
    return result

print(solution())