def solution():
    # Calculate the number of times Jenny has won against Mark
    wins_against_mark = 10 - 1  # Jenny has won 10 times and Mark has won only once

    # Calculate the number of times Jenny has played against Jill
    games_with_jill = 2 * 10  # Jenny has played Jill twice as many times as Mark

    # Calculate the number of times Jenny has won against Jill
    wins_against_jill = int(games_with_jill * 0.75)  # Jill has won 75% of the games with Jenny

    # Calculate the total number of wins by Jenny
    total_wins = wins_against_mark + wins_against_jill
    result = total_wins
    return result

print(solution())