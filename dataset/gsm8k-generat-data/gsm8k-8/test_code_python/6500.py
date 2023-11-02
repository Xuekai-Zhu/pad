def solution():
    # Calculate the number of wins in the first 100 matches
    first_100_wins = 0.5 * 100

    # Calculate the number of wins in the next 100 matches
    next_100_wins = 0.6 * 100

    # Calculate the total number of wins
    total_wins = first_100_wins + next_100_wins
    result = total_wins
    return result

print(solution())