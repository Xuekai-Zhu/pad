def solution():
    """A soccer team has 24 players. They have scored 150 goals on the season. There have been 15 games played. 1/3 of the players have averaged 1 goal each per game. How many total goals have the other players scored?"""
    # Define the total number of players and the number of games played
    total_players = 24
    games_played = 15

    # Calculate the number of players who averaged 1 goal per game
    players_with_goals = total_players // 3

    # Calculate the number of goals scored by those players
    goals_by_players = players_with_goals * games_played

    # Calculate the total number of goals scored by the other players
    total_goals = 150 - goals_by_players

    # return the result
    result = total_goals
    return result

print(solution())