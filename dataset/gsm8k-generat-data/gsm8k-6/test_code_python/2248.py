def solution():
    # Calculate the number of wins in the second competition
    second_comp_wins = (5/8) * 40  # they won 5/8 times as many games as they won in their first competition

    # Calculate the number of wins in the third competition
    third_comp_wins = 40 + second_comp_wins  # they won the same number of games as the sum of the first and second competition winnings

    # Calculate the total wins in the three competitions
    total_wins = 40 + second_comp_wins + third_comp_wins

    result = total_wins
    return result

print(solution())