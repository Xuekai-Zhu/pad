def solution():
    """A basketball team won 40 games in their last competition. In the next competition, they won 5/8 times as many games as they won in their first competition. In the third competition, they won the same number of games as the sum of the first and second competition winnings. Calculate the total number of wins they had in the three competitions."""
    competition1_wins = 40
    competition2_wins = (5/8) * competition1_wins
    competition3_wins = competition1_wins + competition2_wins
    total_wins = competition1_wins + competition2_wins + competition3_wins
    result = total_wins
    return result

print(solution())