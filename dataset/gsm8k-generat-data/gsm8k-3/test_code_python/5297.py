def solution():
    """A soccer team has 24 players. They have scored 150 goals on the season. There have been 15 games played. 1/3 of the players have averaged 1 goal each per game. How many total goals have the other players scored?"""
    # Define the number of players, goals, and games
    num_players = 24
    num_goals = 150
    num_games = 15

    # Calculate the number of players who have averaged 1 goal per game
    num_players_1_goal = num_players // 3

    # Calculate the number of goals scored by these players
    goals_1_goal_players = num_players_1_goal * num_games

    # Calculate the number of goals scored by the other players
    goals_other_players = num_goals - goals_1_goal_players

    # Display the number of goals scored by the other players
    result = goals_other_players
    return result

print(solution())