def solution():
    """
    Archie holds the school record for most touchdown passes with 89 in a season of 16 games. Richard is close to breaking the record, having averaged 6 touchdowns a game in the first 14 games. How many touchdowns per game must he average in the final two games to beat Archie's record?
    """
    archie_record = 89
    num_games = 16
    num_games_played = 14
    num_touchdowns_played = 6 * num_games_played
    num_touchdowns_remaining = archie_record - num_touchdowns_played
    num_games_remaining = num_games - num_games_played
    touchdowns_per_game = num_touchdowns_remaining / num_games_remaining
    result = touchdowns_per_game
    return result

print(solution())