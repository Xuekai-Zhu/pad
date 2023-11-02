def solution():
    """In Sam's first 100 matches he won 50% of matches. In his next 100 games, he won 60% of matches. How many total matches did he win?"""
    first_100_matches_won = 100 * 0.5
    next_100_matches_won = 100 * 0.6
    total_matches_won = first_100_matches_won + next_100_matches_won
    result = total_matches_won
    return result

print(solution())