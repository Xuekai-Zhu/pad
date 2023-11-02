def solution():
    """Chloe and Max played Mario Kart together. The ratio of Chloe’s wins to Max’s wins is 8:3. Chloe won 24 times. How many times did Max win?"""
    chloe_wins = 24
    chloe_max_ratio = 8 / 3
    max_wins = chloe_wins / chloe_max_ratio - chloe_wins
    result = max_wins
    return result

print(solution())