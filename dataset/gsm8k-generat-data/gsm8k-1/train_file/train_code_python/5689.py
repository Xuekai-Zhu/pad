def solution():
    """Fred has 12 identical candy bars, and Uncle Bob has 6 more. If Jacqueline has ten times the total number of candy bars Fred and Uncle Bob have, what's 40% of Jacqueline's candy bars?"""
    fred_candy_bars = 12
    uncle_bob_candy_bars = fred_candy_bars + 6
    total_candy_bars = fred_candy_bars + uncle_bob_candy_bars
    jacqueline_candy_bars = total_candy_bars * 10
    percentage = 0.4
    candy_bar_percent = jacqueline_candy_bars * percentage
    result = candy_bar_percent
    return result

print(solution())