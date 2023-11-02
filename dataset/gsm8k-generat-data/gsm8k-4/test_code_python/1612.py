def solution():
    """Paul earns $12.50 for each hour that he works. He then has to pay 20% for taxes and fees.
    After working 40 hours, Paul receives his paycheck. If he spends 15% of his paycheck on gummy bears,
    how much, in dollars, does he have left?"""
    # Calculate the earnings before taxes and fees
    earnings = 12.5 * 40

    # Calculate the amount of taxes and fees
    taxes_fees = earnings * 0.2

    # Calculate the earnings after taxes and fees
    earnings_after_taxes = earnings - taxes_fees

    # Calculate the amount spent on gummy bears
    gummy_bears = earnings_after_taxes * 0.15

    # Calculate the money left after buying gummy bears
    money_left = earnings_after_taxes - gummy_bears

    # Return the result
    result = money_left
    return result

print(solution())