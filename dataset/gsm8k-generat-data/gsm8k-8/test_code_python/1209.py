def solution():
    # Calculate the number of bars used to pay taxes
    tax_bars = 0.10 * 60

    # Calculate the number of bars left after paying taxes
    bars_left = 60 - tax_bars

    # Calculate the number of bars lost in divorce
    bars_lost = 0.50 * bars_left

    # Calculate the number of bars left after divorce
    bars_remaining = bars_left - bars_lost
    result = bars_remaining
    return result

print(solution())