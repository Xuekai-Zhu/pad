def solution():
    # Define Adam's daily earnings
    daily_earnings = 40

    # Calculate the amount of taxes deducted per day
    tax = 0.1 * daily_earnings

    # Calculate Adam's earnings after taxes per day
    earnings_after_tax = daily_earnings - tax

    # Calculate Adam's earnings after taxes for 30 days of work
    earnings_after_tax_30_days = earnings_after_tax * 30

    result = earnings_after_tax_30_days
    return result

print(solution())