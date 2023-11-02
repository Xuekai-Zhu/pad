def solution():
    """Archie holds the school record for most touchdown passes with 89 in a season of 16 games. Richard is close to breaking the record, having averaged 6 touchdowns a game in the first 14 games. How many touchdowns per game must he average in the final two games to beat Archie's record?"""
    archie_record = 89
    games_played = 16
    games_left = 2
    touchdowns_played = games_played * archie_record
    touchdowns_so_far = 6 * 14
    touchdowns_needed = touchdowns_played - touchdowns_so_far
    touchdowns_per_game_needed = touchdowns_needed / games_left
    result = touchdowns_per_game_needed
    return result

print(solution())