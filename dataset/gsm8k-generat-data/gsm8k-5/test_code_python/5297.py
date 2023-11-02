def solution():
    total_players = 24  # The soccer team has 24 players
    total_goals = 150  # The team has scored 150 goals
    total_games = 15  # There have been 15 games played
    avg_goals_per_game = total_goals / total_games  # Calculate the average goals per game for the team

    # Calculate how many players have averaged 1 goal per game
    players_with_1_goal = total_players / 3
    goals_for_1_goal_players = players_with_1_goal * total_games  # Calculate how many goals these players have scored

    # Calculate how many goals the other players have scored
    goals_for_other_players = total_goals - goals_for_1_goal_players

    result = goals_for_other_players
    return result

print(solution())