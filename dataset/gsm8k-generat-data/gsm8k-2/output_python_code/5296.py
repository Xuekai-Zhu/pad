def solution():
    """A soccer team has 24 players. They have scored 150 goals on the season.
    There have been 15 games played. 1/3 of the players have
    averaged 1 goal each per game. How many total goals have the other players scored?"""
    total_players = 24
    total_goals = 150
    total_games = 15

    # Calculate the number of players who scored an average of 1 goal per game
    num_players_with_1_goal_per_game = total_players // 3
    goals_from_players_with_1_goal_per_game = num_players_with_1_goal_per_game * total_games

    # Calculate the total goals scored by the other players
    goals_from_other_players = total_goals - goals_from_players_with_1_goal_per_game

    result = goals_from_other_players
    return result

print(solution())