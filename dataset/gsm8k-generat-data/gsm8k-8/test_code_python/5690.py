def solution():
    # Calculate the total number of candy bars Uncle Bob has
    uncle_bob_candy_bars = 12 + 6

    # Calculate the total number of candy bars Fred and Uncle Bob have
    fred_and_bob_candy_bars = 12 + uncle_bob_candy_bars

    # Calculate the number of candy bars Jacqueline has
    jacqueline_candy_bars = 10 * fred_and_bob_candy_bars

    # Calculate 40% of Jacqueline's candy bars
    candy_bars_40_percent = 0.4 * jacqueline_candy_bars
    result = candy_bars_40_percent
    return result

print(solution())