def solution():
    """Jake earns thrice what Jacob does. If Jacob earns $6 per hour, how much does Jake earn in 5 days working 8 hours a day?"""
    jacob_hourly_earnings = 6
    jake_hourly_earnings = 3 * jacob_hourly_earnings
    total_jake_earnings = jake_hourly_earnings * 8 * 5
    result = total_jake_earnings
    return result

print(solution())