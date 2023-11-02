def solution():
    first_competition_wins = 40  # The team won 40 games in their first competition
    second_competition_wins = (5/8) * first_competition_wins  # They won 5/8 times as many games in the second competition
    third_competition_wins = first_competition_wins + second_competition_wins  # They won the same number of games as the sum of the first two competitions

    # Calculate the total number of wins in the three competitions
    total_wins = first_competition_wins + second_competition_wins + third_competition_wins
    result = total_wins
    return result

print(solution())