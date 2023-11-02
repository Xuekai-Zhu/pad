def solution():
    """Jake earns thrice what Jacob does. If Jacob earns $6 per hour, how much does Jake earn in 5 days working 8 hours a day?"""
    # Define Jacob's earnings
    jacob_earnings_per_hour = 6

    # Calculate Jake's earnings
    jake_earnings_per_hour = jacob_earnings_per_hour * 3

    # Calculate Jake's total earnings for 5 days of work
    jake_total_earnings = jake_earnings_per_hour * 8 * 5

    # Return the result
    result = jake_total_earnings
    return result

print(solution())