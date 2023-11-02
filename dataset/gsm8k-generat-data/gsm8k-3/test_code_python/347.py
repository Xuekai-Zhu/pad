def solution():
    """Adam earns $40 daily in his job. 10% of his money is deducted as taxes. How much money will Adam have earned after taxes after 30 days of work?"""
    # Define Adam's daily earnings and tax rate
    DAILY_EARNINGS = 40
    TAX_RATE = 0.1

    # Calculate Adam's earnings after taxes for each day of work
    earnings_after_tax = DAILY_EARNINGS * (1 - TAX_RATE)

    # Calculate Adam's total earnings after taxes for 30 days of work
    total_earnings = earnings_after_tax * 30

    # Display Adam's total earnings after taxes
    result = total_earnings
    return result

print(solution())