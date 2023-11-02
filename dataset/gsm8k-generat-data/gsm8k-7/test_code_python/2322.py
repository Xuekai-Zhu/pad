def solution():
    archie_touchdowns = 89
    archie_games = 16
    richard_games = 14
    richard_touchdowns = 6 * richard_games

    # Calculate the remaining number of touchdowns Richard needs to beat Archie's record
    remaining_touchdowns = archie_touchdowns - richard_touchdowns

    # Calculate the number of games Richard has left
    remaining_games = archie_games - richard_games

    # Calculate the average number of touchdowns per game Richard needs to beat Archie's record
    touchdowns_per_game = remaining_touchdowns / remaining_games
    result = touchdowns_per_game
    return result

print(solution())