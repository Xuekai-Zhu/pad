def solution():
    """Chloe and Max played Mario Kart together. The ratio of Chloe’s wins to Max’s wins is 8:3. Chloe won 24 times. How many times did Max win?"""
    chloe_wins = 8
    max_wins = 3
    chloe_win_count = 24
    max_win_count = chloe_win_count / (chloe_wins / max_wins)
    result = max_win_count
    return result

print(solution())