def solution():
    """In Sam's first 100 matches he won 50% of matches. In his next 100 games, he won 60% of matches. How many total matches did he win?"""
    # Define the number of matches in each round and the corresponding win percentage
    matches_1 = 100
    win_percentage_1 = 50
    matches_2 = 100
    win_percentage_2 = 60

    # Calculate the number of matches won in each round
    matches_won_1 = matches_1 * (win_percentage_1 / 100)
    matches_won_2 = matches_2 * (win_percentage_2 / 100)

    # Calculate the total number of matches won
    total_matches_won = matches_won_1 + matches_won_2

    # Return the result
    result = total_matches_won
    return result

print(solution())