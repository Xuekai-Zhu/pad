def solution():
    # Jenny played Mark 10 times and he only won once
    mark_wins = 1
    mark_games = 10
    jenny_wins_mark = mark_games - mark_wins

    # Jenny played Jill twice as many times as Mark
    jill_games = 2 * mark_games
    jill_wins = int(jill_games * 0.75)  # Jill wins 75% of the games against Jenny

    # Calculate the total number of games Jenny has won
    jenny_wins_total = jenny_wins_mark + (jill_games - jill_wins)
    result = jenny_wins_total
    return result

print(solution())