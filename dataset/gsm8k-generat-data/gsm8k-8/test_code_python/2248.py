def solution():
    # Calculate the number of wins in the second competition
    first_competition_wins = 40
    second_competition_wins = (5/8) * first_competition_wins

    # Calculate the number of wins in the third competition
    third_competition_wins = first_competition_wins + second_competition_wins

    # Calculate the total number of wins in all three competitions
    total_wins = first_competition_wins + second_competition_wins + third_competition_wins
    result = total_wins
    return result

print(solution())