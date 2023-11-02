def solution():
    """A basketball team won 40 games in their last competition. In the next competition, they won 5/8 times as many games as they won in their first competition. In the third competition, they won the same number of games as the sum of the first and second competition winnings. Calculate the total number of wins they had in the three competitions."""
    # Define the number of wins in the first competition
    first_wins = 40

    # Calculate the number of wins in the second competition
    second_wins = int(5/8 * first_wins)

    # Calculate the number of wins in the third competition
    third_wins = first_wins + second_wins

    # Calculate the total number of wins in the three competitions
    total_wins = first_wins + second_wins + third_wins

    # Display the total number of wins
    result = total_wins
    return result

print(solution())