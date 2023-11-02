def solution():
    """A basketball team won 40 games in their last competition. In the next competition, they won 5/8 times as many games as they won in their first competition. In the third competition, they won the same number of games as the sum of the first and second competition winnings. Calculate the total number of wins they had in the three competitions."""
    first_comp = 40
    second_comp = 5 / 8 * first_comp
    third_comp = first_comp + second_comp
    total_wins = first_comp + second_comp + third_comp
    result = total_wins
    return result

print(solution())