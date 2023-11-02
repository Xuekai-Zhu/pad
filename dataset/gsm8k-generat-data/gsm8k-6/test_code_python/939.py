def solution():
    # calculate the number of students who play basketball
    basketball_players = 20 / 2

    # calculate the number of students who play volleyball
    volleyball_players = (2/5) * 20

    # calculate the number of students who play both games
    both_players = 20 / 10

    # calculate the number of students who do not play either game
    neither_players = 20 - (basketball_players + volleyball_players - both_players)

    result = neither_players
    return result

print(solution())