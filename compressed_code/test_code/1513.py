def solution():
    
    candy_bars_per_day = [10]  
    for i in range(1, 6):
        candy_bars_per_day.append(candy_bars_per_day[i-1] + 4)  
    total_candy_bars = sum(candy_bars_per_day)
    total_dollars = total_candy_bars * 0.1  
    result = total_dollars
    return result

print(solution())