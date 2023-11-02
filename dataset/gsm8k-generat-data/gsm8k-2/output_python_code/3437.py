def solution():
    """Penn operates an ice cream stall for a week. On the first day, she made $10. Every day after that, she made $4 more than the previous day. How much money did Penn make after 5 days?"""
    first_day_earnings = 10
    total_earnings = first_day_earnings
    for i in range(2, 6):
        day_earnings = first_day_earnings + (i-1) * 4
        total_earnings += day_earnings
    result = total_earnings
    return result

print(solution())