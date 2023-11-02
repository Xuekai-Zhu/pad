def solution():
    """Bill gets paid $20 every hour he works up to a total of 40 hours, after which he gets paid double that amount per hour. How much does Bill get paid for a 50-hour workweek?"""
    regular_hours = 40
    regular_rate = 20
    overtime_hours = 10
    overtime_rate = 40
    total_pay = regular_hours * regular_rate
    total_pay += overtime_hours * overtime_rate
    result = total_pay
    return result

print(solution())