def solution():
    """Jame has 60 bars of gold. He uses 10% of them to pay for tax and then loses half of what is left in divorce. How many gold bars does he have left?"""
    # Define the initial number of gold bars
    initial_bars = 60

    # Calculate the number of bars used to pay for tax
    tax_bars = initial_bars * 0.1

    # Calculate the number of bars left after paying for tax
    bars_after_tax = initial_bars - tax_bars

    # Calculate the number of bars lost in divorce
    bars_lost_in_divorce = bars_after_tax * 0.5

    # Calculate the number of bars left after divorce
    bars_left = bars_after_tax - bars_lost_in_divorce

    # return the result
    result = bars_left
    return result

print(solution())