def solution():
    """Adam earns $40 daily in his job. 10% of his money is deducted as taxes. How much money will Adam have earned after taxes after 30 days of work?"""
    # Define Adam's daily earnings and the tax rate
    daily_earnings = 40
    tax_rate = 0.1

    # Calculate Adam's earnings after taxes for one day
    earnings_after_tax = daily_earnings * (1 - tax_rate)

    # Calculate Adam's total earnings after taxes for 30 days of work
    total_earnings = earnings_after_tax * 30

    # Return the result
    result = total_earnings
    return result

print(solution())