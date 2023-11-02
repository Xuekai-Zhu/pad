def solution():
    
    total_bars = 18
    sold_last_week = 5
    sold_this_week = 7
    remaining_bars = total_bars - sold_last_week - sold_this_week
    result = remaining_bars
    return result

print(solution())