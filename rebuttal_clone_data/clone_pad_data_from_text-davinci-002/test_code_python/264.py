def solution():
    """An Italian restaurant earns $600 every weekday and twice as much on the weekend. How much money does it earn by the end of the month?"""
    weekday_earnings = 600
    weekend_earnings = 2 * weekday_earnings
    total_earnings = (weekday_earnings * 5) + (weekend_earnings * 2)
    result = total_earnings
    return result

print(solution())