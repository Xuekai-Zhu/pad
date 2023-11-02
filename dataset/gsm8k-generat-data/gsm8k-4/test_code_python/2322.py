def solution():
    """Archie holds the school record for most touchdown passes with 89 in a season of 16 games. Richard is close to breaking the record, having averaged 6 touchdowns a game in the first 14 games. How many touchdowns per game must he average in the final two games to beat Archie's record?"""
    # Define Archie's record
    archie_record = 89

    # Define the number of games in a season
    season_games = 16

    # Calculate the number of touchdowns Richard has already scored
    richard_touchdowns = 6 * 14

    # Calculate the number of touchdowns Richard needs to beat Archie's record
    remaining_touchdowns = archie_record - richard_touchdowns

    # Calculate the number of games remaining in the season
    remaining_games = season_games - 14

    # Calculate the average number of touchdowns Richard needs to score in the remaining games
    touchdowns_per_game = remaining_touchdowns / remaining_games

    # Round up to the nearest whole number
    result = math.ceil(touchdowns_per_game)
    return result

print(solution())