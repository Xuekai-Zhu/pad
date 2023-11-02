def solution():
    """Penn operates an ice cream stall for a week. On the first day, she made $10. Every day after that, she made $4 more than the previous day. How much money did Penn make after 5 days?"""
    first_day = 10
    increase_per_day = 4
    days = 5
    total_money = first_day
    for i in range(1, days):
        total_money += (first_day + increase_per_day * i)
    result = total_money
    return result

print(solution())