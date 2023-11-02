def solution():
    """A basketball team won 40 games in their last competition. In the next competition, they won 5/8 times as many games as they won in their first competition. In the third competition, they won the same number of games as the sum of the first and second competition winnings. Calculate the total number of wins they had in the three competitions."""
    # Find the number of games won in the second competition
    second_competition = (5/8) * 40

    # Find the total number of games won in the first two competitions
    first_and_second = 40 + second_competition

    # Find the total number of games won in all three competitions
    total_wins = first_and_second + (first_and_second)

    result = total_wins
    return result

print(solution())