def solution():
    """In Sam's first 100 matches he won 50% of matches.  In his next 100 games, he won 60% of matches.  How many total matches did he win?"""
    # Calculate the number of matches Sam won in the first 100 games
    matches_won_1 = 0.5 * 100

    # Calculate the number of matches Sam won in the next 100 games
    matches_won_2 = 0.6 * 100

    # Calculate the total number of matches won
    total_matches_won = matches_won_1 + matches_won_2

    # Display the total number of matches won
    result = total_matches_won
    return result

print(solution())