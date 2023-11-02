def solution():
    fred_candy_bars = 12
    uncle_bob_candy_bars = fred_candy_bars + 6
    total_candy_bars = fred_candy_bars + uncle_bob_candy_bars
    jacqueline_candy_bars = 10 * total_candy_bars
    percentage = 40
    candy_bars_percentage = (percentage / 100) * jacqueline_candy_bars
    result = candy_bars_percentage
    return result

print(solution())