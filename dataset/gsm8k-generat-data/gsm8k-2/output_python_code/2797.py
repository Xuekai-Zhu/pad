def solution():
    """John works 12 hours every other day. He gets a 30% raise from his former $20 an hour job. How much does he make in a 30 day month?"""
    work_days = 15  # John works every other day, so in a 30-day month he works 15 days.
    hours_per_day = 12
    hourly_rate = 20
    raise_percent = 0.3
    new_rate = hourly_rate * (1 + raise_percent)
    total_pay = work_days * hours_per_day * new_rate
    result = total_pay
    return result

print(solution())