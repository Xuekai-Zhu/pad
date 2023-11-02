def solution():
    """Greg bought a 20-pack of granola bars to eat at lunch for the week. He set aside one for each day of the week, traded three of the remaining bars to his friend Pete for a soda, and gave the rest to his two sisters. How many did each sister get when they split them evenly?"""
    total_bars = 20
    bars_per_day = 7
    bars_left = total_bars - bars_per_day
    bars_traded = 3
    bars_given = bars_left - bars_traded
    bars_per_sister = bars_given / 2
    result = bars_per_sister
    return result

print(solution())