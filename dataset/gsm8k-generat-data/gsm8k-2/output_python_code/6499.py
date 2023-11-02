def solution():
    """In Sam's first 100 matches he won 50% of matches. In his next 100 games, he won 60% of matches. How many total matches did he win?"""
    first_100_win = 0.5 * 100
    next_100_win = 0.6 * 100
    total_win = first_100_win + next_100_win
    result = total_win
    return result

print(solution())