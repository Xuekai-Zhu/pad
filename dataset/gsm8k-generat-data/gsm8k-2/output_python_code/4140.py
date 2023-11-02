def solution():
    """James has 18 chocolate bars to sell for the swim team. He sold 5 last week and 7 this week. How many more chocolate bars does he need to sell?"""
    total_bars = 18
    sold_last_week = 5
    sold_this_week = 7
    remaining_bars = total_bars - sold_last_week - sold_this_week
    result = remaining_bars
    return result

print(solution())