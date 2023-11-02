def solution():
    fred_candy_bars = 12
    uncle_bob_candy_bars = fred_candy_bars + 6
    total_candy_bars = fred_candy_bars + uncle_bob_candy_bars
    jacqueline_candy_bars = total_candy_bars * 10
    
    # Calculate 40% of Jacqueline's candy bars
    forty_percent = 0.4
    forty_percent_of_jacqueline = jacqueline_candy_bars * forty_percent
    result = forty_percent_of_jacqueline
    return result

print(solution())