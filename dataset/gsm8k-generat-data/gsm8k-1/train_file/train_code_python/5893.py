def solution():
    """An employee makes 30 dollars an hour for the first 40 hours in the workweek and an additional 50% for every hour above 40 in the week. If he works 6 hours for the first 3 days in the workweek and twice as many hours per day for the remaining 2 days, how much money did he make?"""
    pay = 0
    base_pay_rate = 30
    regular_hours = 40
    overtime_rate = base_pay_rate * 1.5
    
    # Calculate pay for first 3 days
    pay += (6 * base_pay_rate) * 3
    
    # Calculate pay for remaining 2 days
    hours_remaining = 40 - (3 * 6)
    hours_remaining += 2 * (8 + 8)  # 2 days with 16 hours each
    if hours_remaining > 40:
        pay += regular_hours * base_pay_rate
        pay += (hours_remaining - 40) * overtime_rate
    else:
        pay += hours_remaining * base_pay_rate
    
    result = pay
    return result

print(solution())