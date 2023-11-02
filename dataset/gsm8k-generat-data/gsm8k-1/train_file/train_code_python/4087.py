def solution():
    """Bill gets paid $20 every hour he works up to a total of 40 hours, after which he gets paid double that amount per hour. How much does Bill get paid for a 50-hour workweek?"""
    regular_hours = 40
    overtime_hours = 50 - regular_hours
    regular_pay_rate = 20
    overtime_pay_rate = 2 * regular_pay_rate
    regular_pay = regular_hours * regular_pay_rate
    overtime_pay = overtime_hours * overtime_pay_rate
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())