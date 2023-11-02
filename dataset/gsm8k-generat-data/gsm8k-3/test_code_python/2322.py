def solution():
    """Archie holds the school record for most touchdown passes with 89 in a season of 16 games. Richard is close to breaking the record, having averaged 6 touchdowns a game in the first 14 games. How many touchdowns per game must he average in the final two games to beat Archie's record?"""
    # Define Archie's touchdown record and the number of games played
    ARCHIE_RECORD = 89
    GAMES_PLAYED = 16

    # Define Richard's average touchdown per game and number of games played so far
    RICHARD_AVG_TDS = 6
    RICHARD_GAMES_PLAYED = 14

    # Calculate Richard's current total touchdowns
    current_tds = RICHARD_AVG_TDS * RICHARD_GAMES_PLAYED

    # Calculate the remaining number of games and touchdowns needed
    remaining_games = GAMES_PLAYED - RICHARD_GAMES_PLAYED
    remaining_tds = ARCHIE_RECORD - current_tds

    # Calculate the required average touchdowns per game
    required_avg_tds = remaining_tds / remaining_games

    # Display the required average touchdowns per game
    result = required_avg_tds
    return result

print(solution())