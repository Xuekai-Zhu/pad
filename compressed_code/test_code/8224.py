def solution():
    

    initial_marbles = 24
    lost_marbles = 4
    given_away_marbles = 2 * lost_marbles
    dog_ate_marbles = lost_marbles / 2

    remaining_marbles = initial_marbles - lost_marbles - given_away_marbles - dog_ate_marbles

    result = remaining_marbles
    return result

print(solution())